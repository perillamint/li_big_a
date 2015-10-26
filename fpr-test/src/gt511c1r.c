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

int gt511c1r_open(struct gt511c1r *obj)
{
  char buf[1024];
  struct gt511c1r_packet packet;

  gt511c1r_fill_packet(&packet, 0x00000000, 0x0001);

  obj -> do_usrt(obj -> fd, &packet, 12, buf, 12);

  for(int i = 0; i < 12; i++) {
    printf("0x%02X ", buf[i]);
  }
  printf("\n");

  return 0;
}

int gt511c1r_set_led(struct gt511c1r *obj, uint32_t param)
{
  char buf[1024];
  struct gt511c1r_packet packet;

  gt511c1r_fill_packet(&packet, param, 0x0012);

  obj -> do_usrt(obj -> fd, &packet, 12, buf, 12);

  for(int i = 0; i < 12; i++) {
    printf("0x%02X ", buf[i]);
  }
  printf("\n");
}
