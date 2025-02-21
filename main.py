# RGB-Blink

from machine import Pin
from neopixel import NeoPixel
import time

pin= Pin(48,Pin.OUT) #set GPIO48 to output to drive Neopixel

neo= NeoPixel(pin,1) #create Neopixel driver on GPIO48 for 1 pixel

while True:
    
 neo[0]=(255,0,0) # set the first pixel to white
 neo.write()
 time.sleep(.1)
 neo[0]=(0,255,0)
 neo.write()
 time.sleep(.1)
 neo[0]=(0,0,255)
 neo.write()
 time.sleep(.1)
 


 #write data to all pixels
