# Code to get the pressure, temperature, and altitude from the BMP180 sensor.
# This code gets these values from one sensor and prints them on the screen.

# Sensor: BMP180
# VIN: 3.3V
# GND: GND
# SCL: GP2
# SDA: GP3

from machine import Pin, I2C, SoftI2C
from bmp085 import BMP180
import time

i2c = SoftI2C(sda = Pin(3), scl = Pin(2), freq = 100000) 

bmp = BMP180(i2c)        
bmp.oversample = 2
bmp.sealevel = 101325

while True: 
  start_time = time.ticks_ms() #get the start time
  tempC = bmp.temperature    #get the temperature in degree celsius
  pres_hPa = bmp.pressure    #get the pressure in hpa
  altitude = bmp.altitude    #get the altitude
  temp_f= (tempC * (9/5) + 32)  #convert the temperature value in fahrenheit
  end_time = time.ticks_ms()  #get the end time
  print(str(tempC)+"°C " +str(temp_f)+"°F " + str(pres_hPa)+"hPa "+ str(altitude) + "m" + " Time: " + str(end_time - start_time) + "ms")
  time.sleep_ms(100)  #delay of 100 milliseconds