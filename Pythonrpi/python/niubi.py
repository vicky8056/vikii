
from ubidots import  ApiClient
import  RPi.GPIO as GPIO
import math
import time
import datetime

api=ApiClient(token='BBFF-xHJFyqFYgA52R0Deglq8bDuau8nGQo')
led=api.get_variable('60110bfb1d84723aca104e80')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
    last_value = led.get_values(1)
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
