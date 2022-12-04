# sending data points for ball tracker

from easy_comms import Easy_comms
from time import sleep
import time
from machine import Pin, ADC
import json

hrs=time.localtime()[3]
mins=time.localtime()[4]
secs=time.localtime()[5]
m_secs=time.localtime()[6]
print (str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
command = {'command':'blink', 'args': 'on'}
conversion_factor = (1 / 6553) * 10


com1 = Easy_comms(0,9600)
calibration_pin=ADC(26).read_u16()
percent0 = calibration_pin * conversion_factor
prcalib26b = adc_28 * conversion_factor
#sending calibration value
com1.send(str(prcalib26b))
pr27b=" "
pr28b=" "
#first resistor
while True:
    #com1.send(str(56.0))
    adc_27=ADC(27).read_u16()
    percent27b = adc_27 * conversion_factor

    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent27b-prcalib26b)>=2.0):
        pr27b=(str(abs(percent27b-prcalib26b))+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
        break
    
#second resistor
while True:
    #com1.send(str(56.0))
    adc_28=ADC(28).read_u16()
    percent28b = adc_28 * conversion_factor

    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent28b-prcalib26b)>=2.0):
        pr28b=(str(abs(percent28b-prcalib26b))+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
        com1.send(pr27b+"\n"+pr28b)
        break