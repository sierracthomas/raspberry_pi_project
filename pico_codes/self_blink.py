from machine import Pin, Timer
import time

led = machine.Pin("LED", machine.Pin.OUT)
led.on()
time.sleep(1)
led.off()
