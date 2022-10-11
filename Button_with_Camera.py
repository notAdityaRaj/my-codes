import RPi.GPIO as GPIO
import time
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Define variable and assign the GPIO pins
#Here GPIO4 is connected to Button pin
Button = 4

#Camera declaration
camera = picamera.PiCamera()
#Setting the GPIO4 as input pin to detect when a button is pressed
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Setting the GPIO17 as output pin to turn on the Buzzer
GPIO.setup(17,GPIO.OUT)

try:
#While loop to continuously detects for button press
   while True:
  #Declare a variable input_state and assign it to button state
    input_state = GPIO.input(Button)
    if input_state == 0:
      print ("####### Button Pressed ########")
      print ("Capturing the photo")
      print ("Smile Please !!!")
      time.sleep(2)
      #Save the photo to the mentioned path
      camera.capture('/home/pi/Desktop/image.jpg')
      print ("Photo is captured")
      time.sleep(0.2)
    else:
      print ("Press the button once")
      time.sleep(0.2)
except KeyboardInterrupt:
  print ("Quit")
  GPIO.cleanup()
