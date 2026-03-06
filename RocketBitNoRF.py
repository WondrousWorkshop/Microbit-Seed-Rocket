from microbit import *
import utime
import math
import music

def parachuteOpenen():   
    pin0.write_analog(115)

def luikOpenen():   
    pin1.write_analog(115)

def totaleVersnelling():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    return math.sqrt(x**2 + y**2 + z**2)

platform = 0 #staat stil op het platform
vertrokken = 1 #heeft een Y as G piek gehad
buffer = 2 # dubbelcheck of de je echt aan het vallen bent 
parachute = 3 #de parachute wordt geopend
cargoDrop = 4 #het cargo luik wordt geopend
geland = 5 #unit ligt stil op de grond

vertrokkenDrempel = 2000 #2G
vallenDrempel = 150 #0,15G

wachtTijd = 1000 #1 seconde
timer = 0
grondTimer = 0

pin0.set_analog_period(20)
pin1.set_analog_period(20)

pin0.write_analog(25)
pin1.write_analog(25)

status = platform

while True:
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
