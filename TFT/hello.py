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
SPEED_HZ = 16000000


# Raspberry Pi configuration.
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

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

# Create a blank image with a white background.
img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))

# Initialize the drawing context.
draw = ImageDraw.Draw(img)

# Choose a font and size.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

# Draw the text on the image.
draw.text((20, 70), "Hello", font=font, fill=(0, 0, 0))

# Display the image on the TFT display.
disp.display(img)
