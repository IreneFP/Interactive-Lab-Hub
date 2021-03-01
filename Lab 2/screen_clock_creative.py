import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from datetime import datetime
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
# font_size = 40
font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
# font = ImageFont.truetype("/usr/share/fonts/truetype/Roboto-Black.ttf", 40)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

seconds = 0
start = 0
end = 6
color = "#FFFFFF"

def white_hair(sec):
    return (1.7**(sec/100)) - 1

while seconds < 60:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 
    x0 = 53
    y0 = 0
    x1 = 187 
    y1 = 134
    x_center_text = width/2 - 20/2
    y_center_text = height/2 - 20/2

    xy = [x0, y0, x1, y1]
    draw.arc(xy, start, end, fill=color)
    draw.pieslice(xy, start, end, fill=color)
    
    now = datetime.now()
    seconds = now.second
    white_hair_now = white_hair(seconds)
    draw.text((x_center_text, y_center_text), white_hair_now, font=font_big, fill="#000000", stroke_fill="#FFFFFF", stroke_width=2)
    draw.text((x_center_text, y_center_text+25), "White Hair", font=font_small, fill="#000000", stroke_fill="#FFFFFF", stroke_width=2)
    
    TIME = strftime("%S")
    draw.text((0, top), TIME, font=font_small, fill="#FFFFFF", stroke_width=2)
    
    # Display image.
    disp.image(image, rotation)
    seconds += 1
    end += 6
    if seconds == 59:
        seconds = 0
        if color == "#FFFFFF":
            color = "#000000"
        else:
            color = "#FFFFFF"
        # color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    time.sleep(1)

