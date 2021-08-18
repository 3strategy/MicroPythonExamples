from machine import Pin, PWM  # you may ignore the interpreter error re PWM on pycharm.
import utime

# based on https://www.explainingcomputers.com/sample_code/Servo_Test.py
# PIN SETUP:
#   servo red should always go to 5v (servos use 4.8-6v. Note: strong servos should be powered via a dedicated power supply)
#   servo black should go to ground
#   servo PWM signal should be on a PWM pin, e.g. GP0 in current example

# .duty_16(#) takes values of 0 to 65535 for duty cycle of 0 to 100
# SG90 servo has 2 per cent duty cycle for 0 degrees, 12 per cent for 180.
# So a .duty_u16 value of c.1350 is zero degrees; 8200 is 180 degrees.

servo = PWM(Pin(0))

servo.freq(50)

while True:
    # Move servo to zero degrees (2 per cent duty cycle)
    servo.duty_u16(3350)  # 1350 is the minimal position
    utime.sleep(2)
    # Move servo to 180 degrees (12 per cent duty cycle)
    servo.duty_u16(7200)  # is maximal position
    utime.sleep(2)
    print("end of cycle")
