from ubidots import  ApiClient
import  Rpi.GPIO as GPIO
import math
import time
import datetime

api=ApiClient(token='BBFF-tdqFGUr1OEiDfi3C87ieg4raRoPCUu')
led1=api.get_variable('5ff98e291d84723c053baa49')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)

while True:
    last_value = le1.get_values(1)
    if last_value[0].get("value")==1:
       GPIO.output(19,GPIO.HIGH)
       print('LED is ON')
       time.sleep(0.5)
    else:
      GPIO.output(19,GPIO.LOW)
      print('LED is OFF')
      time.sleep(0.5)
