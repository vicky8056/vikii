import pubnub
try :
  p=pubnub(publish_key="pub-c-9cdda524-55d8-482b-a135-76f7b99378e4 ",subscribe_key="sub-c-46ede5a4-44e2-11eb-9ec5-221b84410db5")
  def callback(message,channel):
    print(message)
  def connect(message):
    print("connected")



    d=p.publish(channel="Nivas_channel",message="hello pubnub")
  
    print(d)
  def error(message):
      print("error" +str(message))
  def reconnect(message):
    print("reconnect")
  def disconnect(message):
    print("disconnect")

  p.subscribe(channel="Nivas_channel",callback=callback,error=callback,connect=connect,reconnect=reconnect,disconnect=disconnect)
except TypeError as t:
      print("this message of error",t)
finally:
     print("close the connection")

