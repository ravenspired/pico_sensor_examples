# Code to get the pressure, temperature, and altitude from three BMP180 sensors.
# This code gets these values from three sensors by taking readings many times and averaging them for each sensor, and prints them on the screen.

# Sensor 1: BMP180
# VIN: 3.3V
# GND: GND
# SCL: GP8
# SDA: GP9

# Sensor 2: BMP180
# VIN: 3.3V
# GND: GND
# SCL: GP2
# SDA: GP3

# Sensor 3: BMP180
# VIN: 3.3V
# GND: GND
# SCL: GP6
# SDA: GP7

from machine import Pin, I2C, SoftI2C
from bmp085 import BMP180
import time

i2c1 = SoftI2C(sda = Pin(9), scl = Pin(8), freq = 100000) 
bmp1 = BMP180(i2c1)        
bmp1.oversample = 2
bmp1.sealevel = 101325

i2c2 = SoftI2C(sda = Pin(3), scl = Pin(2), freq = 100000) 
bmp2 = BMP180(i2c2)        
bmp2.oversample = 2
bmp2.sealevel = 101325

i2c3 = SoftI2C(sda = Pin(6), scl = Pin(7), freq = 100000) 
bmp3 = BMP180(i2c3)        
bmp3.oversample = 2
bmp3.sealevel = 101325

def get_tempC(sensor, times):
    temps_C = []
    divisor = times
    for i in range(times):
        try:
            temps_C.append(sensor.temperature)
        except:
            divisor -= 1
    if divisor == 0:
        return 0
    return sum(temps_C)/divisor

def get_pres_hPa(sensor, times):
    pres_hPa = []
    divisor = times
    for i in range(times):
        try:
            pres_hPa.append(sensor.pressure)
        except:
            divisor -= 1
    if divisor == 0:
        return 0
    return sum(pres_hPa)/divisor

def get_altitude(sensor, times):
    altitude = []
    divisor = times
    for i in range(times):
        try:
            altitude.append(sensor.altitude)
        except:
            divisor -= 1
    if divisor == 0:
        return 0
    return sum(altitude)/divisor



while True: 
    print("Temperature, Sensors 1, 2, 3: " + str(get_tempC(bmp1, 25)) + "C" + ", " + str(get_tempC(bmp2, 25)) + "C" + ", " + str(get_tempC(bmp3, 25)) + "C")
    print("Pressure, Sensors 1, 2, 3: " + str(get_pres_hPa(bmp1, 25)) + "hPa" + ", " + str(get_pres_hPa(bmp2, 25)) + "hPa" + ", " + str(get_pres_hPa(bmp3, 25)) + "hPa")
    print("Altitude, Sensors 1, 2, 3: " + str(get_altitude(bmp1, 25)) + "m" + ", " + str(get_altitude(bmp2, 25)) + "m" + ", " + str(get_altitude(bmp3, 25)) + "m")
    time.sleep(0.5)
    

