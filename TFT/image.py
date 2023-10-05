#VCC - 3.3V - Pin 17
#GND - GND - Pin 6
#CS - Pin 24
#RST - Pin 22
#A0/DC - Pin 18
#SDA/MOSI - Pin 19
#SCK/SCLK - Pin 23
#LED - 3.3V - Pin 1
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


WIDTH = 128
HEIGHT = 160
SPEED_HZ = 4000000
MESSAGE = "Hello World! How are you today?"

# Raspberry Pi configuration.
DC = 24
RST = 22
SPI_PORT = 0
SPI_DEVICE = 0

# BeagleBone Black configuration.
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Create TFT LCD display class.
disp = TFT.ST7735(
    DC,
    rst=RST,
    spi=SPI.SpiDev(
        SPI_PORT,
        SPI_DEVICE,
        max_speed_hz=SPEED_HZ))

# Initialize display.
disp.begin()

# Load an image.
print('Loading image...')
image = Image.open('Hilda.jpg')


# Resize the image and rotate it so matches the display.
image = image.rotate(0).resize((WIDTH, HEIGHT))

# Draw the image on the display hardware.
print('Drawing image')
disp.display(image)
