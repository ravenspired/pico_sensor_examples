from machine import Pin
from utime import sleep_ms
button = Pin(28, Pin.IN, Pin.PULL_UP)   #Internal pull-up
                    
                    
def check_button_press():
    if button.value() == 0:       #key press
        return True     
    else:
        return False
    
    
    
if __name__ == '__main__':
    while True:
        print(check_button_press())
        sleep_ms(10)
