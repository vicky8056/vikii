from Adafruit_CharLCD import Adafruit_CharLCD # Importing Adafruit library for LCD
from time import sleep  # Importing sleep from time library to add delay in program

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=0, en=29, d4=22, d5=23, d6=24, d7=25, cols=16, lines=2)
lcd.clear()
# display text on LCD,  \n = new line
lcd.message('welcome')
sleep(2)

# scroll text on display
try:
    while 1:
        for x in range(0, 16):
            lcd.move_left()
            sleep(0.1)
        sleep(2)    
        # scroll Right
        for x in range(0, 16):
            lcd.move_right()
            sleep(0.1)
        sleep(3)

# If Keyboard Interrupt command is pressed
except KeyboardInterrupt:
    pass

# Clear the screen
lcd.clear()
