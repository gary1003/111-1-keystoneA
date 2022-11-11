from irsensor import IRSensor
from motors import Motors
from hcsr04 import HCSR04
from adxl345 import ADXL345
from machine import Pin, I2C

ir_left = IRSensor(36)
#BRW ORG GRY WHT
my_car = Motors(16,17,18,19)
us = HCSR04(trigger_pin=5, echo_pin=21, echo_timeout_us=10000)
acc = ADXL345(I2C(1))

while True:
    my_car.forward()
    time.sleep(0.1)
    my_car.left()
    time.sleep(0.1)
    my_car.right()
    time.sleep(0.1)    
