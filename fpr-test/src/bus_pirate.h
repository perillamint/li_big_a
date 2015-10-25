//Magic words

static const int  binary_mode_magic_size = 20;
static const char binary_mode_magic[] = {
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};

//Bus pirate UART flags
#define BP_BINARY_RESET         0b00000000
#define BP_BINARY_EXIT          0b00001111

#define BP_UART_MODE            0b00000011

#define BP_UART_RXEN            0b00000010
#define BP_UART_RXDIS           0b00000011

#define BP_UART_BAUD            0b01100000
#define BP_UART_BAUD_2400       0b00000010
#define BP_UART_BAUD_4800       0b00000011
#define BP_UART_BAUD_9600       0b00000100
#define BP_UART_BAUD_19200      0b00000101
#define BP_UART_BAUD_31250      0b00000110
#define BP_UART_BAUD_38400      0b00000111
#define BP_UART_BAUD_57600      0b00001000
#define BP_UART_BAUD_115200     0b00001010

#define BP_UART_SETTINGS        0b10000000
#define BP_UART_SETTINGS_NOPU   0b00000000
#define BP_UART_SETTINGS_3V3PU  0b00010000
#define BP_UART_SETTINGS_8N1    0b00000000
#define BP_UART_SETTINGS_8E1    0b00000100
#define BP_UART_SETTINGS_8O1    0b00001000
#define BP_UART_SETTINGS_9N1    0b00001100
#define BP_UART_SETTINGS_8N2    0b00000010
#define BP_UART_SETTINGS_8E2    0b00000110
#define BP_UART_SETTINGS_8O2    0b00001010
#define BP_UART_SETTINGS_9N2    0b00001110
#define BP_UART_SETTINGS_RXHOT  0b00000000
#define BP_UART_SETTINGS_RXCOLD 0b00000001

#define BP_UART_PERIPHERALS     0b01000000
#define BP_UART_PERIPHERALS_PWR 0b00001000
#define BP_UART_PERIPHERALS_PUP 0b00000100
#define BP_UART_PERIPHERALS_AUX 0b00000010
#define BP_UART_PERIPHERALS_CS  0b00000001

#define BP_UART_BULKWRITE       0b00010000

#define BP_UART_BRIDGE_MODE     0b00001111

int bp_exit_binary(int fd);
int bp_enter_uart_binary(int fd);
int bp_uart_set_power(int fd, int power);
int bp_do_usrt(int fd, char *tx, int txlen, char *rx, int rxlen);
