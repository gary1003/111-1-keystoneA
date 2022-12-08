from irsensor import IRSensor
import time

ir_left = IRSensor(32)
ir_right = IRSensor(33)

while True:

    print("left", ir_left.read())
    print("right", ir_right.read())
    time.sleep(0.1)