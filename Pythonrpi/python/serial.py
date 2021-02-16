from time import sleep
import serial
serialport = serial("serial0", baudrate=9600, timeout=3.0)
while True:
    serialport.write("rnSay something:")
    print("uart transmit")
    rcv = port.read(10)
    serialport.write("rnYou sent:" + repr(rcv))
    sleep(2)
