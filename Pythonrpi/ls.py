import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
#from RPLCD import CursorMode
from time import sleep
GPIO.setwarnings(False)
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23],numbering_mode=GPIO.BOARD)
#lcd.cursor_pos=(1,3)
lcd.write_string(u'vector india')
#lcd.cursor_mode=CursorMode.hide
#sleep(2)
#lcd.clear()
