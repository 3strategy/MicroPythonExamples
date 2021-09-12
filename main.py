#This code is for ESP32 (all builds before were made and tested on PiPico).
#Note that PyCharm has huge issues connecting and sending builds to the ESP32.
#Use Thonny!!!
from machine import Pin
import time

led = Pin(2, Pin.OUT)  # similar setting of pin 25 to OUTPUT
                        # note that such a function returns an object, but also modifies this object.
                        # this is more Object Oriented than the comparable Arduino blink native code
sw = Pin(0, Pin.IN)

# another example of blinking the internal led.
# previous code was from https://github.com/raspberrypi/pico-micropython-examples/blob/master/blink/blink.py#L1-L9
# this version is from https://themachineshop.uk/getting-started-with-the-pi-pico-and-pycharm/

while True:
    led(1)
    time.sleep(0.5)  # this sleep code better resembles the more traditional MCU c code
    led(0)
    time.sleep(0.1)
    print(sw.value(),'ggg')
