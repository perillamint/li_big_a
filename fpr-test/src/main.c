#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>

#include <sys/stat.h>
#include <fcntl.h>

#include "bus_pirate.h"
#include "gt511c1r.h"

const static struct option long_options[] = {
  {"disable-bus-pirate", required_argument, NULL, 1 },
  {"enable-ioctl"      , required_argument, NULL, 2 },
  {NULL                , 0                , NULL, 0 }
};

static int  bus_pirate_flag = 1;
static int  ioctl_flag      = 0;
static char *device_file    = NULL;

void print_usage(char *bin_name)
{
  fprintf(stderr,
          "Usage   : %s [OPTION] [Character device file]\n\n"
          "Options : --disable-bus-pirate (true|false)\n"
          "          --enable-ioctl       (true|false)\n\n"
          "Note    : Bus pirate mode is enabled by default.\n", bin_name);

  exit(1);
}

int do_usrt(int fd, void *tx, int txlen, void *rx, int rxlen)
{
  if(bus_pirate_flag)
    {
      return bp_do_usrt(fd, tx, txlen, rx, rxlen);
    }
  else
    {
      //TODO: Normal UART stuff.
      write(fd, tx, txlen);
    }
}

int main(int argc, char **argv)
{
  for(;;)
    {
      int options_index = 0;
      int c = getopt_long(argc, argv, ":", long_options, &options_index);

      if(c == -1)
        break;

      if(c == 1 || c == 2)
        {
          if(optarg == NULL)
            {
              print_usage(argv[0]);
            }

          if(strncmp("true", optarg, 5) == 0)
            {
              if(c == 1)
                bus_pirate_flag = 0;
              if(c == 2)
                ioctl_flag = 1;
            }
        }
    }

  if (optind + 1 != argc) {
    print_usage(argv[0]);
  }

  device_file = malloc(strlen(argv[optind])+1);
  memcpy(device_file, argv[optind], strlen(argv[optind])+1);

  //Initialization complete!

  int devicefd = open(device_file, O_RDWR);

  if(devicefd == -1)
    {
      fprintf(stderr, "E: Cannot open device %s\n", device_file);
      exit(1);
    }
  printf("Device file: %s\n", device_file);

  if(bus_pirate_flag)
    {
      bp_enter_uart_binary(devicefd);
      bp_uart_set_power(devicefd, 1);
    }

  struct gt511c1r fpr;
  gt511c1r_init(&fpr, devicefd, do_usrt);
  gt511c1r_open(&fpr);
  gt511c1r_set_led(&fpr, 0x00000001);

  //TODO: Display interactive console.

  if(bus_pirate_flag)
    {
      //      bp_exit_binary(devicefd);
    }
  close(devicefd);
  return 0;
}
