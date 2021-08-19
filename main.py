from machine import Pin, PWM, Timer  # you may ignore the interpreter error re PWM on pycharm.
import utime
# when you code is terminal intensive (you need the printouts) I find Thonny to be better suited.
# Reminder: to open the terminal (REPL) from py charm: Tools>MicroPython>MicroPython REPL

# PIN SETUP:
#   servo white (signal) to pin 0 (red to 5v black to GND)
#   resistor (220-500 Ohm) to pin 14, and then to led. led is connected to GND)
#   push switch connected to pin 5 and 3.3v.
#     ->for more details about setting up the switch see https://youtu.be/TDj2kcSA-68?t=335

servo = PWM(Pin(0))
servo.freq(50)

led = Pin(14, Pin.OUT)

switch = Pin(5, Pin.IN, Pin.PULL_DOWN)  # pulling down the pin is important.

timer = Timer()
timer2 = Timer()

def blink(timer):
    led.toggle()

def servomove(timer2):
    servo.duty_u16(4500)  # 1350 is the minimal position 8200 is maximal position
    utime.sleep(3)  # note that during this sleep time the led does not blink.
                    # and the switch status does not print.
                    # HOMEWORK: Why? how do we fix that?
    servo.duty_u16(5000)

timer.init(freq=6.5, mode=Timer.PERIODIC, callback=blink)
timer2.init(freq=0.2, mode=Timer.PERIODIC, callback=servomove)

while True:
    print(switch.value())  # notice again how this DOES NOT WORK when the servo function is "busy working".
    utime.sleep(0.1)