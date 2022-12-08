from irsensor import IRSensor
from motors_analog import Motors
from hcsr04 import HCSR04
from adxl345 import ADXL345
from machine import Pin, I2C
import time

ir_left = IRSensor(32)
ir_right = IRSensor(33)

#BRW ORG GRY WHT
my_car = Motors(16,17,18,19)
us = HCSR04(trigger_pin=5, echo_pin=21, echo_timeout_us=10000)
acc = ADXL345(I2C(1))

start = time.time()

while ((time.time() - start) < 10):
    # print("left", ir_left.read())
    # print("right", ir_right.read())
    # print("distance", us.distance_cm())
    # print("acceleration", acc.get_values())
    # if too close, stop
    distance = us.distance_cm()
    print("distance", distance)
    if distance < 10:
        my_car.stop()
        time.sleep(0.1)
        continue
    # if too far, go forward
    else:
        print('left', ir_left.read())
        print('right', ir_right.read())
        # if left sensor sees black, and right sensor sees white turn right
        if ir_left.read() > 50 and ir_right.read() < 50:
            my_car.right()  
        # if right sensor sees black, and left sensor sees white turn left
        elif ir_right.read() > 50 and ir_left.read() < 50:
            my_car.left()
        # if both sensors see white, go forward
        elif ir_right.read() < 50 and ir_left.read() < 50:
            my_car.forward()
        # if both sensors see black, stop
        else:
            my_car.stop()
        time.sleep(0.01)

my_car.stop()