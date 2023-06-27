from machine import UART
import time
from machine import Pin

# this class measures CO2 with up to 2 MH-Z19B sensors
class MHZ19BSensor:

    # initializes a new instance
    def __init__(self, tx_pin, rx_pin, uartnum, co2_threshold):
        self.uart = UART(uartnum, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(tx_pin), rx=Pin(rx_pin))
        self.lights = 1
        self.co2_threshold = int(co2_threshold)

    # measure CO2
    def measure(self):
        while True:
            # send a read command to the sensor
            self.uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')

            # a little delay to let the sensor measure CO2 and send the data back
            time.sleep(1)  # in seconds

            # read and validate the data
            buf = self.uart.read(9)
            if self.is_valid(buf):
                break

            # retry if the data is wrong

            print('error while reading MH-Z19B sensor: invalid data')
            print('retry ...')



        co2 = buf[2] * 256 + buf[3]
        print('co2         = %.2f' % co2)


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
    
    



mySensor1 = MHZ19BSensor(4, 5, 1, 5)
mySensor2 = MHZ19BSensor(12, 13, 0, 5)
while True:
    print("Sensor 1")
    mySensor1.measure()
    print("Sensor 2")
    mySensor2.measure()
    time.sleep(1)
