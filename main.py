from machine import Pin, PWM, Timer  # you may ignore the interpreter error re PWM on pycharm.
import utime

# PIN SETUP:
#   servo white (signal) to pin 0 (red to 5v black to GND)
#   resistor (220-500 Ohm) to pin 14, and then to led. led is connected to GND)

servo = PWM(Pin(0))
servo.freq(50)

led = Pin(14, Pin.OUT)
timer = Timer()
timer2 = Timer()

def blink(timer):
    led.toggle()

def servomove(timer2):
    servo.duty_u16(3350)  # 1350 is the minimal position 8200 is maximal position
    utime.sleep(3)  # note that during this time the led does not blink. Why? how do we fix that?
    servo.duty_u16(5300)

timer.init(freq=6.5, mode=Timer.PERIODIC, callback=blink)
timer2.init(freq=0.2, mode=Timer.PERIODIC, callback=servomove)
