#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os

LDRpin=18
PWMpin=12

DEBUG = 1
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWMpin, GPIO.OUT)
p = GPIO.PWM(PWMpin, 0.5) #50 % duty cycle to start
p.start(1)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

try:
    while True:
            #RCtime(18)     # Read RC timing using pin #18
            dutyCycle=100*(rctimeMax/RCtime(LDRpin))
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)


#cleanup:
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
