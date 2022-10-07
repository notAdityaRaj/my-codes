"""
Connect the RED_LED Anode to GPIO14
Connect the YELLOW_LED Anode to GPIO17
Connect the GREEN_LED Anode to GPIO23
Connect the ground to GND
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

count = 1
while count<=10:
    GPIO.output(14,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(23,GPIO.LOW)
    count+=1
