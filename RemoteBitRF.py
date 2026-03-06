from microbit import *
import radio
import utime

radio.on()
radio.config(group=2,power=7)

laatsteA = 0
laatsteB = 0
KnopInterval = 500

display.show(Image.HEART)
sleep(1000)
display.clear()

while True:
    nu = utime.ticks_ms()

    # --- ZENDEN: Noodknoppen ---
    if button_a.was_pressed():
        if utime.ticks_diff(nu, laatsteA) < KnopInterval:
            radio.send("P") # Zend Parachute commando!
        laatsteA = nu

    if button_b.was_pressed():
        if utime.ticks_diff(nu, laatsteB) < KnopInterval:
            radio.send("C") # Zend Cargo commando!
        laatsteB = nu
        
    message = radio.receive()
    if message:
        status = int(message)
        if status == 0:
            display.show(Image('90000:'
                               '90000:'
                               '90000:'
                               '90000:'
                               '90000'))
        elif status == 1:
            display.show(Image('99000:'
                               '99000:'
                               '99000:'
                               '99000:'
                               '99000'))
        elif status == 2:
            display.show(Image('99900:'
                               '99900:'
                               '99900:'
                               '99900:'
                               '99900'))
        elif status == 3:
            display.show(Image('99990:'
                               '99990:'
                               '99990:'
                               '99990:'
                               '99990'))            
        elif status == 4:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))        
        
  
