#Wiring
#MOSI - PIN 11
#MISO - PIN 12
#SCLK - PIN 10
#CS - PIN 13



from machine import Pin, SPI
import sdcard
import os
import random
 
#Initialize the onboard LED as output
led = machine.Pin(25,machine.Pin.OUT)

# Toggle LED functionality
def BlinkLED(timer_one):
    led.toggle()
    
def generate_random_floats(size):
    random_floats = []
    for _ in range(size):
        random_floats.append(random.uniform(1, 100))
    return random_floats
    
# Initialize the SD card
spi=SPI(1,baudrate=40000000,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
sd=sdcard.SDCard(spi,Pin(13))

# Create a instance of MicroPython Unix-like Virtual File System (VFS),
vfs=os.VfsFat(sd)
 
# Mount the SD card
os.mount(sd,'/sd')

# Debug print SD card directory and files
print(os.listdir('/sd'))

# Create / Open a file in write mode.
# Write mode creates a new file.
# If  already file exists. Then, it overwrites the file.
file = open("/sd/sample.csv","a")

# Write sample text
col = 10
row = 200
line = ",".join(str(num) for num in generate_random_floats(col)) + "\n"
for i in range(row):
    file.write(line)
    print(i)
    
# Close the file
file.close()
