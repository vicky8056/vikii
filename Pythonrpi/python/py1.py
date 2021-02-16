import pubnub as Pubnub
try :
  p=Pubnub(publish_key="pub-c-3cf0298b-7ac0-4930-bf6c-129ae24319a6 ",subscribe_key="sub-c-ff63ed0e-4744-11eb-9ec5-221b84410db5")
  def _callback(message,channel):
	    print(message)
  def connect(message):
    print("connected")

    d=p.publish(channel="Gopi",message="hello pubnub",callback=_callback,error=_callback)
    print(d)
  def error(message):
      print("error" +str(message))
  def reconnect(message):
    print("reconnect")
  def disconnect(message):
    print("disconnect")

  p.subscribe(channels="Gopi",callback=_callback,error=_callback,connect=connect,reconnect=reconnect,disconnect=disconnect)
except TypeError as t:
      print("this message of error",t)
finally:
     print("close the connection")


