"""
Connect the LED Anode to GPIO14
Connect the ground to GND
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

count = 1
while count<=10:
    GPIO.output(14,GPIO.HIGH)
    print("LED is ON")
    time.sleep(3)
    GPIO.output(14,GPIO.LOW)
    print("LED is OFF")
    time.sleep(3)
    count+=1

