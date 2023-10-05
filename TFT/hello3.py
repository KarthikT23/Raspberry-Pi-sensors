from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


WIDTH = 128
HEIGHT = 160
SPEED_HZ = 16000000

MESSAGE = "Hello World! How are you today?"

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

# Choose a font and increase the size.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 6)

# Initialize y-coordinate for the top of the text.
y = 0

# Split the message into lines.
lines = MESSAGE.split("\n")

# Draw each line of the message starting from the top.
for line in lines:
    # Get the size of the text to be displayed.
    text_width, text_height = draw.textsize(line, font=font)

    # Calculate the x-coordinate to center the text horizontally.
    x = (WIDTH - text_width) // 2

    # Draw the text on the image.
    draw.text((x, y), line, font=font, fill=(0, 0, 0))

    # Increment the y-coordinate for the next line.
    y += text_height

# Display the image on the TFT display.
disp.display(img)