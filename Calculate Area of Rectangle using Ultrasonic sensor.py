import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 16
ECHO = 20
L = 0
W = 0
print("Distance Measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def ultrasonic_sensing():
  for i in range(1,3):
    GPIO.output(TRIG, False)
    print("Waitng for the sensor to settle")
    time.sleep(1)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
  
    while GPIO.input(ECHO) == 0:
      pulse_start = time.time()
  
    while GPIO.input(ECHO) == 1:
      pulse_end = time.time()
  
    pulse_duration = pulse_end - pulse_start
  
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance


print("Waiting for the sensor to read the lenght: ")
L = ultrasonic_sensing()
time.sleep(5)
W = ultrasonic_sensing()
time.sleep(5)
area = L*W
print("Calculating the area....")
time.sleep(3)
print("The Area of the wall is",area,"Sq.units")
