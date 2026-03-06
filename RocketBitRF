from microbit import *
import utime
import math
import music
import radio

def parachuteOpenen():   
    pin0.write_analog(115)

def luikOpenen():   
    pin1.write_analog(115)

def totaleVersnelling():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    return math.sqrt(x**2 + y**2 + z**2)

platform = 0
vertrokken = 1
buffer = 2
parachute = 3
cargoDrop = 4
geland = 5

vertrokkenDrempel = 2000 #2G
vallenDrempel = 150 #0,15G

wachtTijd = 1000 #1 seconde
timer = 0
grondTimer = 0
radioTimer = 0

pin0.set_analog_period(20)
pin1.set_analog_period(20)

pin0.write_analog(25)
pin1.write_analog(25)

status = platform

radio.config(group=2, power=7)
radio.on()

while True:
    if utime.ticks_ms() >= radioTimer + 100:
        radioTimer = utime.ticks_ms()
        radio.send(str(status))
        
    if status == platform and accelerometer.get_y() >= vertrokkenDrempel:
        status = vertrokken
        display.show(Image('90000:'
                            '90000:'
                            '90000:'
                            '90000:'
                            '90000'))
    elif status == vertrokken and accelerometer.get_y() <= vallenDrempel:   
        status = buffer
        timer = utime.ticks_ms()
        display.show(Image('99000:'
                            '99000:'
                            '99000:'
                            '99000:'
                            '99000'))
    elif  status == buffer:
        if utime.ticks_ms() >= timer + wachtTijd and accelerometer.get_y() <= vallenDrempel:
            status = parachute
            parachuteOpenen()
            display.show(Image('99900:'
                            '99900:'
                            '99900:'
                            '99900:'
                            '99900'))
            timer = utime.ticks_ms() 
    elif status == parachute and utime.ticks_ms() >= timer + 2000 and utime.ticks_ms() < timer + 5000: #luik ga automatisch open na 2 sec. 
        status = cargoDrop
        luikOpenen()            
        display.show(Image('99990:'
                            '99990:'
                            '99990:'
                            '99990:'
                            '99990'))
    elif status in (parachute, cargoDrop) and utime.ticks_ms() >= timer + 5000:
        totaal = totaleVersnelling()
        if totaal > 900 and totaal < 1100:
            if grondTimer == 0:
                grondTimer = utime.ticks_ms()
            elif utime.ticks_ms() >= grondTimer + 1000:
                status = geland
        else: grondTimer = 0    
              
    elif status == geland:
        display.show(Image('99999:'
                            '99999:'
                            '99999:'
                            '99999:'
                            '99999'))  
        music.play(music.BA_DING)
        
        
             

      
