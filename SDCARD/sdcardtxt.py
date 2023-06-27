#Wiring
#MOSI - PIN 11
#MISO - PIN 12
#SCLK - PIN 10
#CS - PIN 13



from machine import Pin, SPI
import sdcard
import os
 
#Initialize the onboard LED as output
led = machine.Pin(25,machine.Pin.OUT)

# Toggle LED functionality
def BlinkLED(timer_one):
    led.toggle()
    
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
file = open("/sd/sample.txt","w")

# Write sample text
for i in range(20000):
    file.write("Sample text = %s\r\n" % i)
    print(i)
    
# Close the file
file.close()