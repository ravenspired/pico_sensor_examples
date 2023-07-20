from machine import Pin, PWM
from time import sleep

IN1 = Pin(27, Pin.OUT)
IN2 = Pin(26, Pin.OUT)


while True:
        IN1.low()  #spin forward
        IN2.high()
        sleep(2)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
        
        IN1.high()  #spin backward
        IN2.low()
        sleep(2)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
    
