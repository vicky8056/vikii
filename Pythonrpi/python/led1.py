from gpiozero import LED
from time import sleep
led=LED(17)
while True:
     led.on()
     print("led is on")    
     sleep(5)
     led.off()
     print("led is off")
     sleep(5)
     

