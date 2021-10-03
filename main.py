#ESP32 code
from machine import Pin
import time

led = Pin(2, Pin.OUT)  # internal led

sw = Pin(0, Pin.IN) #internal boot switch

while True:
    led(1)
    time.sleep(0.6)  # this sleep code better resembles the more traditional MCU c code
    led(0)
    time.sleep(0.1)
    print(sw.value(),'gg1')