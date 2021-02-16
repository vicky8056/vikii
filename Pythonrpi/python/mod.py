from pubnub import Pubnub
p=Pubnub(publish_key="pub-c-3cf0298b-7ac0-4930-bf6c-129ae24319a6 ",subscribe_key="sub-c-ff63ed0e-4744-11eb-9ec5-221b84410db5")
channel='Gopi_Channel'
def callback(message):
     print(message)
p.publish(channel,"Hello pubnub",callback=callback,error=callback)
def error(message):
     print(message)
def _callback(message,channel):
     print(message)
def _error(message):
     print(message)
p.subscribe(channels='Gopi_Channel',callback=_callback,error=_error)
