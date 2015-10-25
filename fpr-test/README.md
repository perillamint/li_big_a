# FPR-test

Note: This testing application is built for testing GT-511C1R through bus pirate.

Currently supported platform is UNIX-like system only. You need to specify device file (e.g. /dev/ttyACM0) for bus pirate.

## Requirements

You need CMake to build this project.

To run this application, you need [Bus pirate](http://dangerousprototypes.com/docs/Bus_Pirate) and [GT-5111C1R](https://www.sparkfun.com/products/13007) fingerprint scanner.

## TODOs

Support FT232 USB to UART dongle using ioctl syscall.
