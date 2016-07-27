#!/usr/bin/env python

# Uses Adafruit's Example for RC timing reading for Raspberry Pi found here:
# https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
#
# The LDR timing controls the duty cycle of a PWM output to a PNP transistor controlling the backlight on a modified 3.5" LCD

import RPi.GPIO as GPIO, time, os
import numpy as np

LDRpin=23
PWMpin=18

LDRtimeMAX=100000
dutyCycleOffset=-1
lowPassAlpha=25
meanLdrTime=0 #startupvalue

GPIO.setmode(GPIO.BCM)

GPIO.setup(PWMpin, GPIO.OUT)
p = GPIO.PWM(PWMpin, 100) #50Hz
p.start(100) #50 % duty cycle to start


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
            rawLdrTime=RCtime(LDRpin)

            print "rawLdrTime:  " + str(rawLdrTime)

            meanLdrTime=((meanLdrTime*lowPassAlpha)+rawLdrTime)/(lowPassAlpha+1)

            meanLdrTime=np.clip(meanLdrTime,0,LDRtimeMAX) #make sure it's within range

            print "meanLdrTime: " + str(meanLdrTime)

            dutyCycle=dutyCycleOffset+100-int(100*(LDRtimeMAX-meanLdrTime)/float(LDRtimeMAX)) #force float division, and then truncate back to integer

            dutyCycle=np.clip(dutyCycle,0,100) #constrain the duty cycle to allowed values

            print "dutycycle:   "+str(dutyCycle)

            p.ChangeDutyCycle(dutyCycle)

            #time.sleep(0.01)


#cleanup:
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
