import RPi.GPIO as GPIO
from time import sleep
ledpin=17
#ledpin3=3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin,GPIO.OUT)
#GPIO.setup(ledpin3,GPIO.IN)
while True:
    GPIO.output(ledpin,GPIO.HIGH)
    print("led on")
    sleep(5)
    GPIO.output(ledpin,GPIO.LOW)
    print("led off")
    sleep(5)
 #   if GPIO.input(ledpin3)==GPIO.HIGH:
  #      print("high")
   # else:
   #     print("low")

