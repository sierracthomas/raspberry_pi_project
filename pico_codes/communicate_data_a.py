# led_client

from easy_comms import Easy_comms
from time import sleep
from machine import Pin, ADC
import json
import time

com1 = Easy_comms(0,9600)
calib_value = []
data_time_array = [[0 for col in range(3)] for row in range(5)]
print(data_time_array)

# recieve message of calibration value and break when done
while True:
    message = com1.read()
    if message is not None:
        try:
            calib_value = float(message)
            print(calib_value)
            break
        except Exception as e:
            print(f'error: {e}')
            break
        
percent0 = calib_value
conversion_factor = (1 / 6553) * 10
#first resistor
while True:
    #com1.send(str(56.0))
    adc_28=ADC(28).read_u16()
    percent1 = adc_28 * conversion_factor

    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent1-percent0)>=2.0):
       str_1=(str(percent1-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       print(str_1)
       break

#second resistor
while True:
    #com1.send(str(56.0))
    adc_26=ADC(26).read_u16()
    percent2 = adc_26 * conversion_factor
    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent2-percent0)>=2.0):
       str_2=(str(percent2-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       print(str_2)
       break

# third resistor
while True:
    #com1.send(str(56.0))
    adc_27=ADC(27).read_u16()
    percent3 = adc_27 * conversion_factor
    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent3-percent0)>=2.0):
       str_3=(str(percent3-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       print(str_3)
       break
    
# recieve message of data points and break when done
while True:
    message = com1.read()
    if message is not None:
        try:
            first_data = message
            print(first_data)
            break
        except Exception as e:
            print(f'error: {e}')
            break

