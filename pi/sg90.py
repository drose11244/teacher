#!/usr/bin/python

import RPi.GPIO as GPIO

import time

SERVO = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(SERVO, GPIO.OUT)

p = GPIO.PWM(SERVO, 50)

p.start(2.5)

try:

    while True:

        p.ChangeDutyCycle(7.5)

        time.sleep(1)

        p.ChangeDutyCycle(12.5)

        time.sleep(1)

        p.ChangeDutyCycle(2.5)

        time.sleep(1)

        print "Done loop"

except KeyboardInterrupt:
	pass

p.stop()

GPIO.cleanup()

