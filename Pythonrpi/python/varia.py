import requests
import random
import time

TOKEN = "BBFF-Trvre2iLUMHGOWpICXoip4NzOO1Yd5" # Assign your Ubidots Token
DEVICE = "Raspberrypi" # Assign the device label to obtain the variable
VARIABLE = "temp" # Assign the variable label to obtain the variable value
DELAY = 1  # Delay in seconds

def get_var(device, variable):
    try:
        url = "http://industrial.api.ubidots.com/"
        url = url + \
            "api/v1.6/devices/{0}/{1}/".format(device, variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        return req.json()['last value']['value']
    except:
        pass


if __name__ == "__main__":
    while True:
        print(get_var(DEVICE, VARIABLE))
        time.sleep(DELAY)
