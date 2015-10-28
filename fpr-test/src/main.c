#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>
#include <termios.h>

#include <signal.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "bus_pirate.h"
#include "gt511c1r.h"

const static struct option long_options[] = {
  {"disable-bus-pirate", required_argument, NULL, 1 },
  {"disable-termiobaud", required_argument, NULL, 2 },
  {NULL                , 0                , NULL, 0 }
};

static int  bus_pirate_flag = 1;
static int  termiobaud      = 1;
static char *device_file    = NULL;

static int devicefd = 0;

void print_usage(char *bin_name)
{
  fprintf(stderr,
          "Usage   : %s [OPTION] [Character device file]\n\n"
          "Options : --disable-bus-pirate (true|false)\n"
          "          --disable-termiobaud (true|false)\n\n"
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

void do_cleanup()
{
  if(bus_pirate_flag)
    {
      bp_exit_binary(devicefd);
    }

  close(devicefd);
  exit(0);
}

int main(int argc, char **argv)
{
  signal(SIGINT, do_cleanup);

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
                termiobaud = 1;
            }
        }
    }

  if (optind + 1 != argc) {
    print_usage(argv[0]);
  }

  device_file = malloc(strlen(argv[optind])+1);
  memcpy(device_file, argv[optind], strlen(argv[optind])+1);

  //Initialization complete!

  devicefd = open(device_file, O_RDWR);

  if(devicefd == -1)
    {
      fprintf(stderr, "E: Cannot open device %s\n", device_file);
      exit(1);
    }
  printf("Device file: %s\n", device_file);

  if(termiobaud)
    {
      struct termios options;
      speed_t speed = B9600;

      if(bus_pirate_flag)
        {
          speed = B115200;
        }

      tcgetattr(devicefd, &options);
      cfsetispeed(&options, speed);
      cfsetospeed(&options, speed);
      tcsetattr(devicefd, TCSANOW, &options);
    }

  if(bus_pirate_flag)
    {
      bp_enter_uart_binary(devicefd);
      bp_uart_set_power(devicefd, 1);
      fprintf(stderr, "Entered BP binary mode.\n");
    }

  struct gt511c1r fpr;
  gt511c1r_init(&fpr, devicefd, do_usrt);
  gt511c1r_open(&fpr);

  int userinput = 0;
  int id = 0;

  for(;;)
    {
      printf("Input number\n"
             "0 - Exit program\n"
             "1 - Clear fingerprint memory\n"
             "2 - Enroll finger\n"
             "3 - Identify finger\n"
             "select>");
      scanf("%d", &userinput);

      switch(userinput)
        {
        case 0:
          do_cleanup();
        case 1:
          gt511c1r_delete_all_fingerprint(&fpr);
          break;
        case 2:
          printf("Input slot number: ");
          scanf("%d", &userinput);
          if(userinput < 0 || userinput > 19)
            {
              printf("Wrong number!\n");
              break;
            }
          gt511c1r_enroll_fingerprint(&fpr, userinput);
          break;
        case 3:
          printf("Identifying!\n");
          id = gt511c1r_identify_fingerprint(&fpr);
          printf("Identified as fingerprint #%d\n", id);
          break;
        default:
          printf("Not in range!\n");
        }
    }

  //TODO: Display interactive console.

  sleep(1);
  do_cleanup();
  return 0;
}
