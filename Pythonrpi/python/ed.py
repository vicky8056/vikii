import RPi.GPIO as GPIO
from time import sleep
import sys
from pubnub import Pubnub
GPIO.setmode(GPIO.BCM)
ledpin=17
GPIO.setup(ledpin,GPIO.OUT)
p=Pubnub(publish_key="pub-c-3cf0298b-7ac0-4930-bf6c-129ae24319a6 ",subscribe_key="sub-c-ff63ed0e-4744-11eb-9ec5-221b84410db5")
channel='Gopi_Channel'
def _callback(m,channel):
      print(m)
      if m['led']==1:
              for i in range(6):
                  GPIO.output(ledpin,True)
                  sleep(0.5)
                  GPIO.output(ledpin,False)
                  sleep(0.5)
def _error(m):
       print(m)
p.subscribe(channels=channel,callback=_callback,error=_error)

