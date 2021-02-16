from RPLCD import CharLCD
import RPi.GPIO as GPIO

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35,
              pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)
# please note that numbering_mode can not be None in latest version of RPLCD

lcd.write_string(u'Hello World')
