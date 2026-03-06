from microbit import *
import utime

platform = 0 #staat stil op het platform
vertrokken = 1 #heeft een Y as G piek gehad
buffer = 2 # dubbelcheck of de 
vrijeval = 3 #ervaart minder dan de normale zwaartekracht op y
parachute = 4 #de parachute is geopend
geland = 5 #ligt stil op de grond

status = platform

vertrokkenDrempel = 2000
vallenDrempel = 0


wachtTijd = 1000 #1 seconde
timer = 0



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
    elif status == parachute and utime.ticks_ms() >= timer + wachtTijd:
        luikOpen()
        display.show(Image('99990:'
                            '99990:'
                            '99990:'
                            '99990:'
                            '99990'))
      
parachuteOpenen() #beschrijf wat er gebeurd als de parachute activeerd wordt.    

luikOpenen() #beschrijf wat er gebeurd als het luik gactiveerd wordt.
