#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT) 
 
#GPIO.output(4, GPIO.HIGH) 

GPIO.output(4, GPIO.LOW)

