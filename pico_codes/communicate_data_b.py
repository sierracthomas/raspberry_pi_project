# led_server

from easy_comms import Easy_comms
from time import sleep
import utime
from machine import Pin, ADC
import json

#print(int(time.time()*1000))
#sleep(0.1)
#print(int(time.time()*1000))



command = {'command':'blink', 'args': 'on'}
conversion_factor = (1 / 6553) * 10


com1 = Easy_comms(0,9600)
calibration_pin=ADC(28).read_u16()

prcalib28b = calibration_pin * conversion_factor
calib_time=utime.ticks_ms()
#sending calibration value
com1.send(str(prcalib28b))
pr27b=" "
pr26b=" "
adc_26=ADC(26).read_u16()
percent26b = adc_26 * conversion_factor
print(percent26b)
adc_27=ADC(27).read_u16()
percent27b = adc_27 * conversion_factor
print(percent27b)    
    
    
#first resistor
while True:
    #com1.send(str(56.0))
    adc_26=ADC(26).read_u16()
    percent26b = adc_26 * conversion_factor
    m_secs=utime.ticks_ms()
    if(abs(percent26b-prcalib28b)>=3.0):
        print(percent26b)
        pr26b=(str(abs(percent26b-prcalib28b))+" "+str(m_secs-calib_time))
        break
#second resistor
while True:
    #com1.send(str(56.0))
    adc_27=ADC(27).read_u16()
    percent27b = adc_27 * conversion_factor
    m_secs=utime.ticks_ms()
    if(abs(percent27b-prcalib28b)>=3.0):
        print(percent27b)
        pr27b=(str(abs(percent27b-prcalib28b))+" "+str(m_secs-calib_time))
        break
    
com1.send(pr26b)
sleep(.2)
com1.send(pr27b)
    