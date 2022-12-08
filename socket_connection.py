from adxl345 import ADXL345
from machine import I2C
import time
import socket

SERVER_IP = ("192.168.4.2", 7414)
acc = ADXL345(I2C(1))

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(0.1)
    client.bind(('0.0.0.0', '7414'))
    client.sendto('team TA', SERVER_IP)
    _start = client.recvfrom(1024)[0].decode()
    if _start == 'start':
        start_time = time.time()
        while((time.time() - start_time) <= 10):
            print(acc.get_values())
            client.sendto(str(acc.get_values()), SERVER_IP)
            time.sleep(0.1)
        client.sendto('stop', SERVER_IP)
            
except Exception as e:
    print(e)
    
            
