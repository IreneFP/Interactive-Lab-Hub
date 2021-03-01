import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import random


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
# font = ImageFont.truetype("/usr/share/fonts/truetype/Roboto-Black.ttf", 40)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

seconds = 0
start = 0
end = 6
color = "#FFFFFF"
while seconds < 60:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 
    x0 = 53
    y0 = 0
    x1 = 187 
    y1 = 134

    xy = [x0, y0, x1, y1]
    draw.arc(xy, start, end, fill= color)
    draw.pieslice(xy, start, end, fill= color)
    TIME = strftime("%S")
    draw.text((width/2, height/2), TIME, font=font, fill="#FFFFFF", stroke_fill="#000000")
    
    # DATE = strftime("%m/%d/%Y")
    # TIME = strftime("%H:%M:%S")
    # y = top # Y position
    # draw.text((x, y), DATE, font=font, fill="#FFFFFF")
    # y = font.getsize(DATE)[1]
    # draw.text((x, y), TIME, font=font, fill="#0000FF")
    
    # Display image.
    disp.image(image, rotation)
    seconds += 1
    end += 6
    if seconds == 59:
        seconds = 0
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(10)]
    time.sleep(1)

