#include <stdint.h>

struct gt511c1r_packet {
  uint8_t  cmdmag[2];
  uint16_t device_id;
  uint32_t param;
  uint16_t command;
  uint16_t checksum;
};

struct gt511c1r {
  int fd;
  int (*do_usrt)(int fd, void *tx, int txlen, void *rx, int rxlen);
};

void gt511c1r_calc_checksum(struct gt511c1r_packet *packet);
int gt511c1r_verify_checksum(struct gt511c1r_packet *packet);
int gt511c1r_init(struct gt511c1r *obj, int fd,
                  int (*do_usrt)(int fd, void *tx, int txlen,
                                 void *rx, int rxlen));
int gt511c1r_open(struct gt511c1r *obj);
int gt511c1r_set_led(struct gt511c1r *obj, uint32_t param);
