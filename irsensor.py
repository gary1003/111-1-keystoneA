from machine import Pin, ADC

class IRSensor:
    
    def __init__(self, pin: int):
        try:
            self.sensor = ADC(Pin(pin))
            self.sensor.atten(ADC.ATTN_11DB)
            self.sensor.width(ADC.WIDTH_12BIT)

        except:
            print(f'error starting IRSensor at pin{pin}')
        
    def read(self):
        return self.sensor.read()