#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "gt511c1r.h"

void gt511c1r_calc_checksum(struct gt511c1r_packet *packet)
{
  int packet_size = sizeof(struct gt511c1r_packet) - 2;
  uint8_t *pkt = (uint8_t*) packet;
  uint16_t csum = 0;

  for(int i = 0; i < packet_size; i++)
    csum += pkt[i];

  packet -> checksum = csum;
}

int gt511c1r_verify_checksum(struct gt511c1r_packet *packet)
{
  int packet_size = sizeof(struct gt511c1r_packet) - 2;
  uint8_t *pkt = (uint8_t*) packet;
  uint16_t csum = 0;

  for(int i = 0; i < packet_size; i++)
    csum += pkt[i];

  if(packet -> checksum == csum)
    return 0;

  return 1;
}

void gt511c1r_fill_packet(struct gt511c1r_packet *packet,
                          uint32_t param, uint16_t command)
{
  packet -> cmdmag[0] = 0x55;
  packet -> cmdmag[1] = 0xAA;
  packet -> device_id = 0x0001;
  packet -> param = param;
  packet -> command = command;

  gt511c1r_calc_checksum(packet);
}

int gt511c1r_init(struct gt511c1r *obj, int fd,
                  int (*do_usrt)(int fd, void *tx, int txlen,
                                 void *rx, int rxlen))
{
  obj -> fd = fd;
  obj -> do_usrt = do_usrt;
}

gt511c1r_response gt511c1r_do_command(struct gt511c1r *obj,
                                      uint32_t param, uint16_t command)
{
  struct gt511c1r_packet txpacket;
  struct gt511c1r_packet rxpacket;
  gt511c1r_response retval;

  memset(&retval, 0, sizeof(gt511c1r_response));

  //Build packet
  gt511c1r_fill_packet(&txpacket, param, command);

  //Send command and receive response.
  obj -> do_usrt(obj -> fd, &txpacket, 12, &rxpacket, 12);

  //Verify checksum.
  if(gt511c1r_verify_checksum(&rxpacket) != 0)
    {
      fprintf(stderr, "E: Checksum failure!\n");
      retval.csumfail = 1;
      return retval;
    }

  if(rxpacket.command == 0x30)
    retval.ack = 1;

  retval.param = rxpacket.param;

  return retval;
}

int gt511c1r_open(struct gt511c1r *obj)
{
  //Open command
  if(gt511c1r_do_command(obj, 0x00000000, 0x0001).ack != 1)
    {
      fprintf(stderr, "E: open failure!\n");
      return -1;
    }

  return 0;
}

int gt511c1r_set_led(struct gt511c1r *obj, uint32_t param)
{
  gt511c1r_response resp;

  //CmosLed command
  resp = gt511c1r_do_command(obj, param, 0x0012);
  if(resp.ack != 1)
    {
      fprintf(stderr, "E: CmosLed failure!\n");
      return -1;
    }

  return 0;
}

int gt511c1r_capture_fingerprint(struct gt511c1r *obj, uint32_t param)
{
  gt511c1r_response resp;

  //Turn on LED.
  gt511c1r_set_led(obj, 0x00000001);
  //Wait until press
  do
    {
      printf("Press finger!\n");
      sleep(1);
      resp = gt511c1r_do_command(obj, 0x00000000, 0x0026);
    }
  while(resp.ack && resp.param != 0);

  //Turn on LED.
  gt511c1r_set_led(obj, 0x00000001);
  //CaptureFinger command
  resp = gt511c1r_do_command(obj, param, 0x0060);
  if(resp.ack != 1)
    {
      fprintf(stderr, "E: CaptureFinger failure!\n"
              "Errorcode: 0x%04X\n", resp.param);
      return -1;
    }

  printf("Release finger!\n");
  sleep(1);

  return 0;
}

int gt511c1r_enroll_fingerprint(struct gt511c1r *obj, uint32_t param)
{
  //EnrollStart command
  if(gt511c1r_do_command(obj, param, 0x0022).ack != 1)
    {
      fprintf(stderr, "E: EnrollStart failure!\n");
      return -1;
    }

  //Enroll1-3 command
  for(int i = 0; i < 3; i++)
    {
      fprintf(stderr, "Enrolling #%d\n", i+1);

      if(gt511c1r_capture_fingerprint(obj, 0x00000001) != 0)
        {
          return -1;
        }

      if(gt511c1r_do_command(obj, 0x00000000, 0x0023 + i).ack != 1)
        {
          fprintf(stderr, "E: Enroll%d failed!\n", i+1);
          return -1;
        }
    }

  return 0;
}

int gt511c1r_delete_all_fingerprint(struct gt511c1r *obj)
{
  //DeleteAll command
  if(gt511c1r_do_command(obj, 0x00000000, 0x0041).ack != 1)
    {
      fprintf(stderr, "E: DeleteAll failure!\n");
      return -1;
    }

  return 0;
}

int gt511c1r_identify_fingerprint(struct gt511c1r *obj)
{
  gt511c1r_response resp;

  gt511c1r_capture_fingerprint(obj, 0x00000001);

  resp = gt511c1r_do_command(obj, 0x00000000, 0x0051);
  if(resp.ack != 1)
    {
      fprintf(stderr, "E: Identify failure!\n"
              "Errorcode: 0x%04X\n", resp.param);
      return -1;
    }

  return resp.param;
}
