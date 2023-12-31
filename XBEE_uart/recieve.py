#Source: Electrocredible.com, Language: MicroPython.
from machine import Pin,UART
import time
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=None, stop=2)
led = Pin("LED", Pin.OUT)

while True:
    uart.write('t')
    # print(uart.read())
    if uart.any(): 
        data = uart.read() 
        print(data)
        if data== b'm':
            led.toggle() 
    # time.sleep(1)