#!/usr/bin/python

from gps import GPS

def main():
    gps = GPS(port='com4')

    while True:
        gps.loop()


if __name__ == '__main__':
    main()
