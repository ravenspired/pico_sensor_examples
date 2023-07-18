# Code to get the CO2 PPM from the MH-Z19B sensor, and change the auto calibration sensor if needed. 
# This code sets up 2 sensors, disables automatic calibration, and then reads the CO2 PPM from each sensor.

# Sensor Pinout
# Wire 0: Yellow: NC
# Wire 1: Green: TX
# Wire 2: Blue: RX
# Wire 3: Red: VCC
# Wire 4: Black: GND
# Wire 5: White: NC
# Wire 6: Brown: NC

# Sensor 1: MH-Z19B:
# UART 0
# TX: GP0 (Blue Wire)
# RX: GP1 (Green Wire)

# Sensor 2: MH-Z19B:
# UART 1
# TX: GP4 (Blue Wire)
# RX: GP5 (Green Wire)


from machine import UART
import time
from machine import Pin


class MHZ19BSensor:

    # initializes a new instance
    def __init__(self, tx_pin, rx_pin, uartnum, co2_threshold):
        self.uart = UART(uartnum, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(tx_pin), rx=Pin(rx_pin))
        self.lights = 1
        self.co2_threshold = int(co2_threshold)

    def enable_auto_calibration(self):
        self.uart.write(b'\xff\x01\x79\xa0\x00\x00\x00\x00\xe6')
        time.sleep(1)
    
    def disable_auto_calibration(self):
        self.uart.write(b'\xff\x01\x79\0x00\x00\x00\x00\x00\xe6')
        time.sleep(1)
        
    # measure CO2
    def measure(self):
        while True:
            # send a read command to the sensor
            self.uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')

            # a little delay to let the sensor measure CO2 and send the data back
            time.sleep(.1)  # in seconds

            # read and validate the data
            buf = self.uart.read(9)
            if self.is_valid(buf):
                break

            # retry if the data is wrong

            print('error while reading MH-Z19B sensor: invalid data')
            print('retry ...')



        co2 = buf[2] * 256 + buf[3]
        return co2
        #print('co2         = %.2f' % co2)


    # check data returned by the sensor
    def is_valid(self, buf):
        if buf is None or buf[0] != 0xFF or buf[1] != 0x86:
            return False
        i = 1
        checksum = 0x00
        while i < 8:
            checksum += buf[i] % 256
            i += 1
        checksum = ~checksum & 0xFF
        checksum += 1
        return checksum == buf[8]
    
    



mySensor1 = MHZ19BSensor(0, 1, 0, 5)
mySensor2 = MHZ19BSensor(4, 5, 1, 5)

mySensor1.disable_auto_calibration()
mySensor2.disable_auto_calibration()

while True:
    print("===")
    print("Sensor 1:", mySensor1.measure())
    print("Sensor 2:", mySensor2.measure())
    time.sleep(1)


