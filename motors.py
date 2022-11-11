from machine import Pin, PWM

class Motors:
    
    def __init__(self, pin1, pin2, pin3, pin4):
        
        self.M1A = PWM(Pin(pin1), freq=20000, duty=0)
        self.M1A.init(freq=20000, duty=0)
        self.M1B = PWM(Pin(pin2), freq=20000, duty=0)
        self.M1B.init(freq=20000, duty=0)
        self.M2A = PWM(Pin(pin3), freq=20000, duty=0)
        self.M2A.init(freq=20000, duty=0)
        self.M2B = PWM(Pin(pin4), freq=20000, duty=0)
        self.M2B.init(freq=20000, duty=0)
        self.M1A.duty(0)
        self.M1B.duty(0)
        self.M2A.duty(0)
        self.M2B.duty(0)
    
    def forward(self, speed=1023):
        if speed < 600:
            return
        
        self.M1A.duty(0)
        self.M1B.duty(speed)
        self.M2A.duty(speed)
        self.M2B.duty(0)
        
        
    def left(self, speed=1023):
        if speed < 600:
            return
        self.M1A.duty(0)
        self.M1B.duty((speed-600)//4 + 600)
        self.M2A.duty(speed)
        self.M2B.duty(0)
        
    def right(self, speed=1023):
        if speed < 600:
            return
        self.M1A.duty(0)
        self.M1B.duty(speed)
        self.M2A.duty((speed-600)//4 + 600)
        self.M2B.duty(0)

    def stop(self):
        
        self.M1A.duty(0)
        self.M1B.duty(0)
        self.M2A.duty(0)
        self.M2B.duty(0)