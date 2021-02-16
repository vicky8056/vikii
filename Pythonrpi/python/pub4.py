from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

ENTRY = "Earth"
CHANNEL = "Gopi"
the_update = None

pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-3cf0298b-7ac0-4930-bf6c-129ae24319a6"
pnconfig.subscribe_key = "sub-c-ff63ed0e-4744-11eb-9ec5-221b84410db5"
pnconfig.uuid = "Client-8zise"

pubnub = PubNub(pnconfig)

print("*****************************************")
print("* Submit updates to The Guide for Earth *")
print("*     Enter 42 to exit this process     *")
print("*****************************************")

while the_update != "42":
    print
    the_update = input("Enter an update for Earth: ")
    the_message = {"entry": ENTRY, "update": the_update}
    envelope = pubnub.publish().channel(CHANNEL).message(the_message).sync()

    if envelope.status.is_error():
        print("[PUBLISH: fail]")
        print("error: %s" % status.error)
    else:
        print("[PUBLISH: sent]")
        print("timetoken: %s" % envelope.result.timetoken)
