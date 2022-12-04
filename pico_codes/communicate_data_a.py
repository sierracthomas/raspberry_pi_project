# led_client

from easy_comms import Easy_comms
from time import sleep
from machine import Pin, ADC
import json
import time

com1 = Easy_comms(0,9600)
calib_value = []
data_time_array = [[0 for col in range(3)] for row in range(5)]

#pr1 = Pin(3, Pin.OUT)
#pr1.value(1)


data_time_array[0][2] = .610 # position of first resistor in meters
data_time_array[1][2] = 1.22
data_time_array[2][2] = 1.83
data_time_array[3][2] = 2.44
data_time_array[4][2] = 3.05
print(data_time_array)

# recieve message of calibration value and break when done
while True:
    message = com1.read()
    if message is not None:
        try:
            calib_value = float(message)
            break
        except Exception as e:
            print(f'error: {e}')
            break
        
percent0 = calib_value
conversion_factor = (1 / 6553) * 10
print(ADC(26).read_u16()* conversion_factor)
print(ADC(27).read_u16()* conversion_factor)
print(ADC(28).read_u16()* conversion_factor)
# first resistor

while True:
    #com1.send(str(56.0))
    adc_26=ADC(26).read_u16()
    percent2 = adc_26 * conversion_factor
    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent2-percent0)>=3.0):
       data_time_array[0][0] = float(percent2 - percent0)
       data_time_array[0][1] = float(secs)
       pr26a=(str(percent2-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       print(pr26a)
       break

# second resistor
while True:
    #com1.send(str(56.0))
    adc_27=ADC(27).read_u16()
    percent3 = adc_27 * conversion_factor
    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent3-percent0)>=3.0):
       data_time_array[1][0] = float(percent3 - percent0)
       data_time_array[1][1] = float(secs)
       pr27a=(str(percent3-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       print(pr27a)
       break
 

#third resistor
while True:
    #com1.send(str(56.0))
    adc_28=ADC(28).read_u16()
    percent1 = adc_28 * conversion_factor

    hrs=time.localtime()[3]
    mins=time.localtime()[4]
    secs=time.localtime()[5]
    m_secs=time.localtime()[6]
    if(abs(percent1-percent0)>=3.0):
       data_time_array[2][0] = float(percent1 - percent0)
       data_time_array[2][1] = float(secs)
       pr28a=(str(percent1-percent0)+" "+str(hrs)+":"+str(mins)+":"+str(secs)+":"+str(m_secs))
       print(pr28a)
       break 

# recieve message of data points and break when done
while True:
    message = com1.read()
    if message is not None:
        try:
            data_time_array[3][0] = float(message.split()[0])
            data_time_array[3][1] = float(message.split()[1])
            break
        except Exception as e:
            print(f'error: {e}')
            break
        
# recieve message of data points and break when done
while True:
    message = com1.read()
    if message is not None:
        try:
            data_time_array[4][0] = float(message.split()[0])
            data_time_array[4][1] = float(message.split()[1])
            break
        except Exception as e:
            print(f'error: {e}')
            break
print(data_time_array)
        
# calculate acceleration 

