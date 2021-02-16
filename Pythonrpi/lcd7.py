from RPLCD import CharLCD
from time import sleep
lcd=CharLCD(cols=16,rows=2,pin_rs=37,pin_e=35,pins_data=[40,38,36,32,33,31,29,23])
lcd.cursor_pos=(1,3)
while True:
     lcd.write_string(u'Hello world!')

     sleep(2)
     lcd.clear()
     sleep(2)
