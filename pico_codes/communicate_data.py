# led_server

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
led = Pin("LED", Pin.OUT)
adc_28=ADC(28).read_u16()
calibration_pin=ADC(27).read_u16()
percent0 = calibration_pin * conversion_factor
percent1 = adc_28 * conversion_factor
com1.send("Calibration value: "+str(percent0))
print(adc_28)
str_1=" "
str_2=" "
#first resistor
while True:
    #com1.send(str(56.0))
    adc_28=ADC(28).read_u16()
    calibration_pin=ADC(27).read_u16()
    percent0 = calibration_pin * conversion_factor
    percent1 = adc_28 * conversion_factor

    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    print(percent1)
    if(abs(percent1-percent0)>=2.0):
       str_1=(str(percent1-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       break
    
#second resistor
while True:
    #com1.send(str(56.0))
    adc_26=ADC(26).read_u16()
    calibration_pin=ADC(27).read_u16()
    percent0 = calibration_pin * conversion_factor
    percent1 = adc_26 * conversion_factor

    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    print(percent1)
    if(abs(percent1-percent0)>=2.0):
       str_2=(str(percent1-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       com1.send(str_1+"\n"+str_2)
       break    