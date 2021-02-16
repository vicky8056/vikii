from time import sleep
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

DEVICE = "Raspberrypi"
VARIABLE1 = "temp"
TOKEN = "BBFF-Trvre2iLUMHGOWpICXoip4NzOO1Yd5"
while True:
      light= requests.get("http://things.ubidots.com/api/v1.6/devices/"+DEVICE+"/"+VARIABLE1+"/lv?token="+TOKEN)
      print "Light 1 is now : "+light.content
      if light=="1.0":
          GPIO.output(17,True)
          print("led is on")
      elif light=="0.0":
          GPIO.output(17,False)
          print("led is off")
      sleep(0.5)
