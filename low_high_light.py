from machine import ADC, Pin
from utime import sleep

pr_1 = ADC(26)
calibration_pr = ADC(27)


conversion_factor = (1 / 6553) * 10
 

while True:
    calib_value = calibration_pr.read_u16()
    percent0 = calib_value * conversion_factor
    
    raw1 = pr_1.read_u16()
    percent1 = raw1 * conversion_factor

    #print('Raw: {} '.format(raw1), 'Percent {:2f}%'.format(percent1))
    if (percent0 - percent1 >= 2.0):
        print("low")
    else:
        print("high")
    sleep(0.001) 
