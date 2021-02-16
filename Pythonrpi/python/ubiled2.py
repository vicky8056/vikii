from ubidots import ApiClient
import RPi.GPIO as GPIO

api=ApiClient(token="BBFF-Trvre2iLUMHGOWpICXoip4NzOO1Yd5")
variable=api.get_variable("5ff958a61d847219d88099fa")

last_value=variable.get_values(1)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
print last_value[0]['value']

if last_value==1.0:
    GPIO.output(17,1)
