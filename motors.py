from machine import Pin, PWM

class Motors:
    
    def __init__(self, pin1, pin2, pin3, pin4):

        self.M1A = Pin(pin1, Pin.OUT)
        self.M1B = Pin(pin2, Pin.OUT)
        self.M2A = Pin(pin3, Pin.OUT)
        self.M2B = Pin(pin4, Pin.OUT)
        self.M1A.value(0)
        self.M1B.value(0)
        self.M2A.value(0)
        self.M2B.value(0)

    def forward(self):

        self.M1A.value(1)
        self.M1B.value(0)
        self.M2A.value(1)
        self.M2B.value(0)
    
    def stop(self):
        self.M1A.value(0)
        self.M1B.value(0)
        self.M2A.value(0)
        self.M2B.value(0)
    
    def left(self):
        self.M1A.value(0)
        self.M1B.value(0)
        self.M2A.value(1)
        self.M2B.value(0)

    def right(self):
        self.M1A.value(1)
        self.M1B.value(0)
        self.M2A.value(0)
        self.M2B.value(0)
