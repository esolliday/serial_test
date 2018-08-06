from __future__ import print_function
import string
import serial
import time


def send_command(channel, command):
    channel.write(command)


def read_result(channel):
    s = ''
    char = ''

    # while 1:
    #     size = ser.inWaiting()
    #     if size:
    #         s += ser.read(size)
    #
    #         if string.find(s, '$ ') > 0:
    #             break
    #         size = 0
    #
    while 1:
        size = ser.inWaiting()
        if size:
            char = ser.read(1)
            s += char

            if char == '\n':
                print('I got here')
                print(s, end='')
            else:
                break

            if string.find(s, '$ ') > 0:
                break
            size = 0

    print(s, end='')


ser = serial.Serial('/dev/cu.usbserial-14201', 115200, timeout=5)

send_command(ser, '\n')

read_result(ser)

time.sleep(1)

send_command(ser, 'help\n')

read_result(ser)

ser.close()

print("Done")

