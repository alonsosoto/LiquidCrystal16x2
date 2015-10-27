 import os
 from time import sleep
 
 class Adafruit_CharLCD(object)
     # commands
      if bits[i] == "1":
                self.GPIO.output(self.pins_db[::-1][i], True)
        self.pulseEnable()
        for pin in self.pins_db:
            self.GPIO.output(pin, False)
    
    for pin in self.pins_db:
        self.GPIO.output(pin, False)
         for i in range(4, 8):
             if bits[i] == "1":
                 self.GPIO.output(self.pins_db[::-1][i-4], True)

if __name__ == '__main__':
    lcd = Adafruit_CharLCD()
    ocomando = os.popen('ifconfig | grep Addr')
    agora = ocomando.read()
    
    lcd = Adafruit_CharLCD() 
    lcd.begin(16,2)
    lcd.clear()
    lcd.message(agora)
    lcd.message("Marramiaoo !!!! ")
    lcd.message("hackme!!!\n")
    lcd.message("################")
    lcd.cursor()
    lcd.blink()
    lcd.display()

