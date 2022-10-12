import RPi.GPIO as GPIO
import time
IR_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IR_pin,GPIO.IN)

count = 0
IR = GPIO.input(IR_pin)
while True:
  if IR == 0:
    print("Person detected")
    count+=1
    print(f"No of Visitors: {count}")
    time.sleep(0.2)
  else:
    print("Person not detected")
  
