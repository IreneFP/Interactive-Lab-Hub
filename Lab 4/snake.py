import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
# import adafruit_apds9960.apds9960
from time import strftime, sleep
import random

############### For touch sensors
import busio
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
############### For gesture sensors
# apds = adafruit_apds9960.apds9960.APDS9960(i2c)

# apds.enable_proximity = True
# apds.proximity_interrupt_threshold = (0, 175)
# apds.enable_proximity_interrupt = True

# apds.enable_gesture = True

############### For screen display

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
# font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
# font = ImageFont.truetype("/usr/share/fonts/truetype/Roboto-Black.ttf", 40)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# print("w", width) # w 240
# print("h", height) # h 135

up = 3
down = 0

# while True:
#     gesture = apds.gesture()
 
#     if gesture == 0x01:
#         print("up")
#     elif gesture == 0x02:
#         print("down")
#     elif gesture == 0x03:
#         print("left")
#     elif gesture == 0x04:
#         print("right")

while True:

    goalx1 = 230
    goaly1 = random.randint(10, 125) # random, between 10 and 125

    snakex1 = 0
    snakey1 = random.randint(5, 130) # random, between 5 and 235

    fast = 0

    while True:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        
        goalx2 = goalx1 + 10
        goaly2 = goaly1 + 10

        snakex2 = snakex1 + 20
        snakey2 = snakey1 + 5

        draw.rectangle((snakex1, snakey1, snakex2, snakey2), fill="#FFFFFF")
        draw.rectangle((goalx1, goaly1, goalx2, goaly2), fill="#ffcc00")

        for i in (up, down):
            if mpr121[i].value:
                if i == up:
                    snakey1 -= 5
                if i == down:
                    snakey1 += 5
        
        # gesture = apds.gesture()

        # if gesture == 1 or gesture == 2 or gesture == 3 or gesture == 4:
        #     print("go for it!")
        #     fast = 10
        
        snakex1 += (5 + fast)
        
        disp.image(image, rotation)
        
        time.sleep(0.05)  # Small delay to keep from spamming output messages.
        
        if snakex2 == 230 and snakey1 in range(goaly1, goaly2): # WIN
            
            
            break
        if snakex2 > 240: # LOSE
            
            
            break