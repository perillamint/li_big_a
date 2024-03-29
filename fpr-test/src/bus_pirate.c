#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include "bus_pirate.h"

int bp_send_command(int fd, char cmd)
{
  char buf;

  write(fd, &cmd, 1);
  tcdrain(fd);
  read(fd, &buf, 1);

  if(buf != 0x01)
    {
      fprintf(stderr, "E: BP does not return 0x01. return: 0x%02X\n", buf);
      return -1;
    }

  return 0;
}

int bp_exit_binary(int fd)
{
  char buf[1024];
  char cmd;

  usleep(10000);
  cmd = BP_BINARY_RESET;
  write(fd, &cmd, 1);
  tcdrain(fd);
  read(fd, buf, 5);
  buf[5] = 0;

  if(strncmp(buf, "BBIO1", 5) != 0)
    {
      fprintf(stderr, "E: BP does not return BBIO1. return: %s\n", buf);
      return -1;
    }

  cmd = BP_BINARY_EXIT;
  if(bp_send_command(fd, cmd))
    return -1;
}

/**********************************
 *
 * enter_uart_binary
 *
 * Enter Bus pirate binary UART mode.
 * It also turns on power supply, pullups.
 *
 * Default: 9600 8N1 Hot RX with pullup.
 *
 **********************************/

int bp_enter_uart_binary(int fd)
{
  char buf[1024];
  char cmd = 0;
  struct termios options;

  //Flush command by sending ret.
  //write(fd, "\r\n", 2);
  //Sleep for a bit.
  usleep(1000*500);
  //Flush buffer.
  //usleep(1000*500);
  /*
  fcntl(fd, F_SETFL, FNDELAY);
  read(fd, buf, 1024);
  fcntl(fd, F_SETFL, 0);
  */

  //Enter binary mode.

  write(fd, binary_mode_magic, binary_mode_magic_size);
  tcdrain(fd);
  usleep(10000);
  read(fd, buf, 5);
  buf[5] = 0;

  if(strncmp(buf, "BBIO1", 5) != 0)
    {
      fprintf(stderr, "E: BP does not return BBIO1. return: %s\n", buf);
      return -1;
    }

  cmd = BP_UART_MODE;
  write(fd, &cmd, 1);
  tcdrain(fd);
  usleep(10000);
  read(fd, buf, 4);
  buf[4] = 0;

  if(strncmp(buf, "ART1", 5) != 0)
    {
      fprintf(stderr, "E: BP does not return ART1. return: %s\n", buf);
      return -1;
    }

  cmd = BP_UART_SETTINGS
    | BP_UART_SETTINGS_3V3PU
    | BP_UART_SETTINGS_8N1
    | BP_UART_SETTINGS_RXHOT;

  if(bp_send_command(fd, cmd))
    return -1;

  cmd = BP_UART_BAUD
    | BP_UART_BAUD_9600;

  if(bp_send_command(fd, cmd))
    return -1;

  return 0;
}

int bp_uart_set_power(int fd, int power)
{
  char buf[1024];
  char cmd = 0;

  cmd = BP_UART_PERIPHERALS;
  if(power)
    {
      cmd |= BP_UART_PERIPHERALS_PWR;
      cmd |= BP_UART_PERIPHERALS_PUP;
    }

  if(bp_send_command(fd, cmd))
    return -1;
}

int bp_do_usrt(int fd, void *tx, int txlen, void *rx, int rxlen)
{
  int marker = 0;
  char cmd;
  char buf[1024];

  while(txlen > 0)
    {
      int sendlen = 0;
      cmd = BP_UART_BULKWRITE;

      if(txlen > 16)
        {
          cmd |= 16 - 1;
          txlen -= 16;
          sendlen = 16;
        }
      else
        {
          cmd |= txlen - 1;
          sendlen = txlen;
          txlen = 0;
        }

      if(bp_send_command(fd, cmd))
        return -1;

      write(fd, &((char*)tx)[marker], sendlen);
      tcdrain(fd);
      read(fd, buf, sendlen);

      for(int i = 0; i < sendlen; i++)
        {
          if(buf[i] != 0x01)
            return -1;
        }

      marker += sendlen;
    }

  cmd = BP_UART_RXEN;
  if(bp_send_command(fd, cmd))
    return -1;

  //TODO: Handle exception for this.
  read(fd, rx, rxlen);

  cmd = BP_UART_RXDIS;
  if(bp_send_command(fd, cmd))
    return -1;

  return 0;
}
