from RPLCD import CharLCD 
import RPi.GPIO as GPIO
#from time import sleep
lcd=CharLCD(cols=16,rows=2,pin_rs=37,pin_e=35,pins_data=[33,31,29,23],numbering_mode=GPIO.BOARD)
#lcd.cursor_pos=(1,3)
lcd.write_string(u'Hello world')
#sleep(5)
#lcd.clear()
