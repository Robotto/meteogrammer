#!/usr/bin/env python

# Uses Adafruit's Example for RC timing reading for Raspberry Pi found here: 
# https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
# 
# The LDR timing controls the duty cycle of a PWM output to a PNP transistor controlling the backlight on a modified 3.5" LCD

import RPi.GPIO as GPIO, time, os

LDRpin=23
PWMpin=18

LDRtimeMAX=100000

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
            ldrTime=RCtime(LDRpin)
            # print "ldrTime: " + str(ldrTime)

            if (ldrTime>LDRtimeMAX): #safety feature
                    ldrTime=LDRtimeMAX

            dutyCycle=100-int(100*(LDRtimeMAX-ldrTime)/float(LDRtimeMAX)) #force float division, and then truncate back to integer

            # print "dutycycle: "+str(dutyCycle)

            p.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)


#cleanup:
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
