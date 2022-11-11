from machine import Pin, PWM
import time

led = PWM(Pin(4), freq=20000, duty=0)

for j in range(10):
    for i in range(10):
        led.duty(i)
        time.sleep(0.05)
    for i in range(10):
        led.duty(10-i)
        time.sleep(0.05)

