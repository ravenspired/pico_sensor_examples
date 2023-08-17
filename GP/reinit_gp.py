from machine import Pin

# write code that uses deinit() for every GP pin on rpi pico

# create a list of all the pins
pins = [Pin(i, Pin.OUT) for i in range(28)]

# loop through the list and deinit() each pin
for pin in pins:
    a = pin.OUT

