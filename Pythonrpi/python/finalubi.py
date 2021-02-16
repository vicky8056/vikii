from ubidots import  ApiClient
import  RPi.GPIO as GPIO
import math
import time
import datetime

api=ApiClient(token='BBFF-Trvre2iLUMHGOWpICXoip4NzOO1Yd5')
led1=api.get_variable('5ff98e471d84723da20db41d')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
    last_value = led1.get_values(1)
    if last_value[0].get("value")==1:
       GPIO.output(11,GPIO.HIGH)
       print('LED is ON')
       #time.sleep(0.5)
    elif last_value[0].get("value")==5:
         GPIO.output(11,GPIO.HIGH)
         print('LED is BLINKING')
         time.sleep(1)
         GPIO.output(11,GPIO.LOW)
    else:
      GPIO.output(11,GPIO.LOW)
      print('LED is OFF')
