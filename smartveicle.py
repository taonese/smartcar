#!/usr/bin/env python

import time
import gpio
import socket

IN1="gpio15"
IN2="gpio14"
IN3="gpio16"
IN4="gpio17"


def delay(ms):
    time.sleep(1.0*ms/1000)

def setup():
    gpio.pinMode(IN1,gpio.OUTPUT)
    gpio.pinMode(IN2,gpio.OUTPUT)
    gpio.pinMode(IN3,gpio.OUTPUT)
    gpio.pinMode(IN4,gpio.OUTPUT)

def stop():
    gpio.digitalWrite(IN1,gpio.LOW)
    gpio.digitalWrite(IN2,gpio.LOW)
    gpio.digitalWrite(IN3,gpio.LOW)
    gpio.digitalWrite(IN4,gpio.LOW)

def right():
    gpio.digitalWrite(IN1,gpio.HIGH)
    gpio.digitalWrite(IN2,gpio.LOW)
    gpio.digitalWrite(IN3,gpio.LOW)
    gpio.digitalWrite(IN4,gpio.LOW)
    delay(80)

def left():
    gpio.digitalWrite(IN1,gpio.LOW)
    gpio.digitalWrite(IN2,gpio.LOW)
    gpio.digitalWrite(IN3,gpio.HIGH)
    gpio.digitalWrite(IN4,gpio.LOW)
    delay(80)

def front():
    gpio.digitalWrite(IN1,gpio.HIGH)
    gpio.digitalWrite(IN2,gpio.LOW)
    gpio.digitalWrite(IN3,gpio.HIGH)
    gpio.digitalWrite(IN4,gpio.LOW)

def back():
    gpio.digitalWrite(IN1,gpio.LOW)
    gpio.digitalWrite(IN2,gpio.HIGH)
    gpio.digitalWrite(IN3,gpio.LOW)
    gpio.digitalWrite(IN4,gpio.HIGH)
    
def com():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('0.0.0.0',12345))
    sock.listen(50)
    print 'start TCP server listening 12345'
    while True:
        print 'waiting for client connect'
        connection,address=sock.accept()
        try:
            buf=connection.recv(1024)
            if buf=='left':
                print 'left'
                left()
            if buf=='right':
                print 'right'
                right()
            if buf=='front':
                print 'front'
                front()
            if buf=='back':
                print 'back'
                back()
            if buf=='stop':
                print 'stop'
                stop()
        except socket.timeout:
            print 'time out'
        connection.close()

def loop():
    while True:
        com()

def main():
    setup()
    stop()
    loop()

main() 
