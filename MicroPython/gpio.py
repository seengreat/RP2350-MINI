import machine
import utime

gp0 = machine.Pin(0, machine.Pin.OUT)
gp1 = machine.Pin(1, machine.Pin.OUT)
gp2 = machine.Pin(2, machine.Pin.OUT)
gp3 = machine.Pin(3, machine.Pin.OUT)
gp4 = machine.Pin(4, machine.Pin.OUT)
gp5 = machine.Pin(5, machine.Pin.OUT)
gp6 = machine.Pin(6, machine.Pin.OUT)
gp7 = machine.Pin(7, machine.Pin.OUT)
gp8 = machine.Pin(8, machine.Pin.OUT)
gp9 = machine.Pin(9, machine.Pin.OUT)
gp10 = machine.Pin(10, machine.Pin.OUT)
gp11 = machine.Pin(11, machine.Pin.OUT)
gp12 = machine.Pin(12, machine.Pin.OUT)
gp13 = machine.Pin(13, machine.Pin.OUT)
gp14 = machine.Pin(14, machine.Pin.OUT)
gp15 = machine.Pin(15, machine.Pin.OUT)
gp16 = machine.Pin(16, machine.Pin.OUT)
gp17 = machine.Pin(17, machine.Pin.OUT)
gp18 = machine.Pin(18, machine.Pin.OUT)
gp19 = machine.Pin(19, machine.Pin.OUT)
gp20 = machine.Pin(20, machine.Pin.OUT)
gp21 = machine.Pin(21, machine.Pin.OUT)
gp22 = machine.Pin(22, machine.Pin.OUT)
gp23 = machine.Pin(23, machine.Pin.OUT)
gp24 = machine.Pin(24, machine.Pin.OUT)
gp25 = machine.Pin(25, machine.Pin.OUT)
gp26 = machine.Pin(26, machine.Pin.OUT)
gp27 = machine.Pin(27, machine.Pin.OUT)
gp28 = machine.Pin(28, machine.Pin.OUT)
gp29 = machine.Pin(29, machine.Pin.OUT)

gpio = [gp0, gp1, gp2, gp3, gp4, gp5, gp6, gp7, gp8, gp9, gp10, gp11, gp12, gp13, gp14, gp15, gp16,
        gp17, gp18, gp19, gp20, gp21, gp22, gp23, gp24, gp25, gp26, gp27, gp28, gp29]
while True:

    print("GPIO HIGH")
    for i,pio in enumerate(gpio):    
        pio.value(1)
    utime.sleep(2)
    print("GPIO LOW")
    for i,pio in enumerate(gpio):    
        pio.value(0)
    utime.sleep(2)
