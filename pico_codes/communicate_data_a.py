# led_client

from easy_comms import Easy_comms
from time import sleep
from machine import Pin, ADC
import json
import utime

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
            calib_time = utime.ticks_ms()
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
    m_secs = utime.ticks_ms()
    if(abs(percent2-percent0)>=3.0):
       data_time_array[0][0] = float(percent2 - percent0)
       data_time_array[0][1] = float(m_secs - calib_time)
       pr26a=(str(percent2-percent0)+" "+str(m_secs))
       print(pr26a)
       break

# second resistor
while True:
    #com1.send(str(56.0))
    adc_27=ADC(27).read_u16()
    percent3 = adc_27 * conversion_factor
    m_secs = utime.ticks_ms()
    if(abs(percent3-percent0)>=3.0):
       data_time_array[1][0] = float(percent3 - percent0)
       data_time_array[1][1] = float(m_secs - calib_time)
       pr27a=(str(percent3-percent0)+" "+str(m_secs))
       print(pr27a)
       break
 

#third resistor
while True:
    #com1.send(str(56.0))
    adc_28=ADC(28).read_u16()
    percent1 = adc_28 * conversion_factor
    m_secs = utime.ticks_ms()
    if(abs(percent1-percent0)>=3.0):
       data_time_array[2][0] = float(percent1 - percent0)
       data_time_array[2][1] = float(m_secs - calib_time)
       pr28a=(str(percent1-percent0)+" "+str(m_secs))
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

# calculate velocities
vel = []
time_value = 0
for i in range(0,4):
    distance_value = data_time_array[i+1][2] - data_time_array[i][2]
    time_value = (data_time_array[i+1][1] - data_time_array[i][1]) * 0.001 # convert to s
    vel.append(distance_value/time_value)

print(vel)

acc = []
time_value = 0
for i in range(1,4):
    vel_value = vel[i] - vel[i-1]
    time_value = (data_time_array[i+1][1] - data_time_array[i-1][1]) * 0.001 # convert to s
    acc.append(vel_value/time_value)

print("acceleration values", acc)
print("average a", (acc[0] + acc[1] + acc[2])/3)
# calculate acceleration 

