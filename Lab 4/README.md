# Ph-UI!!!

## ✅ Prep 

Readings: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o)
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/)
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/)
* [Cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) 

### For lab, you will need:

1. Cardboard (start collecting those shipping boxes!)
1. Cutting board
1. Cutting tools
1. Markers
1. Found objects and materials--like bananas--we're not saying that to be funny.


### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
Here are the parts of the assignment

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

# The Report - Part 1

## ✅ Part A
### Capacitive Sensing, a.k.a. Human Banana Interaction

We wanted to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we were able to provide. At boot it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. You can attach any conductive material. In your kit you have conductive fabric and copper tape that will work well, but don't limit yourself! In this lab we will use (go?) bananas!

<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
<img src="https://post.healthline.com/wp-content/uploads/2020/08/banana-pink-background-thumb-1-732x549.jpg" height="150">
</p>

Plug in the capacitive sensor board with the qwiic connector. Connect your banana's with either the copper tape or the alligator clips (the clips work better). make sure to install the requirements from `requirements.txt`

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Banana 10 touched!
Banana 6 touched!
```

## ❎ Part B
### OLED screen

Unfortunately, since the campus closed, I could not get my OLED Screen :(

We just received some of the small oled screens that we had coped to include in your kit. If you want one feel free to pop into the lab and get one. These don't have colors like the one on the pi but you can move it around on a cable making for more flexible interface design. The way you program this display is almost identical to the pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

## ✅ Part C

#### Brainstorming

##### Inspirational Links:

The capacitive sensor offers endless possibilities! And think about it combined with other sensors, like my new recently discovered gesture recognition. Before starting my creation process I did a round of research. Here the websites and porjects I like the most:


- [Raphaël Pluvinage](https://vimeo.com/user3131794) → A big source of inspiration has been this website! I truly recommend you look at it. 

<p float="left">
<img src="inspiration/raphael" height="200" />
</p>

- ["XOXX Composer"](https://www.pinterest.com.mx/pin/804948133376198819/) by Axel Bluhme 

<p float="left">
<img src="inspiration/xoxx" height="200" />
</p>

##### My ideas:

- “Learn how to pronounce words / Learn another language!” game for kids. By touching a certain word, the Pi would pronounce it out loud and the kid would need to repeat it. 


- “Find the pairs! Touch different elements around and uncover their hidden patterns” game. Some elements around would have a hidden pattern, and these patterns are displayed for 1 second in the Pi screen when touching them. You would need to touch different elements in the space you are around and find the patterns that match. 


- “What sound do plants make?” My idea was to attach different plant leaves into a round and conductive surface, in a way that the leaves did have some room to move depending on the wind currents. Then, attach some conductive material behind the leaves so whenever the leaves move with the wind and touch the surface, a sound would be heard!


- “Camera with heat” I still want to do this one!! How can I use [heat-sensitive fabric](https://www.alibaba.com/product-detail/High-quality-heat-sensitive-color-changing_1600086710813.html) or [heat-sensitive paint](https://www.amazon.com/thermochromic-paint/s?k=thermochromic+paint) and this [pin art game](https://www.amazon.com/Rhode-Island-Novelty-Point-Impressions/dp/B002MUYTMG/ref=asc_df_B002MUYTMG/?tag=hyprod-20&linkCode=df0&hvadid=309875729163&hvpos=&hvnetw=g&hvrand=1954434514155065801&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-568944846160&psc=1&tag=&ref=&adgrpid=65715448310&hvpone=&hvptwo=&hvadid=309875729163&hvpos=&hvnetw=g&hvrand=1954434514155065801&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-568944846160) to create pictures? Ideally, I would use the Pi camera to translate the light intensity for each pixel to heat. This heat would be applied to the corresponding pins in the pin art surface, and these would transmit the heat to the fabric. 


- Simon says - I loved that game!


- A Mancala game but with touch.


- Tetris!


- Snake! (my final choice). How can I play the snake game using the movement that BMW (the car brand) popularized, creating what has been named as the best advertisement in history. [Te gusta conducir?](https://images.app.goo.gl/3D1GHZzfAH8m9S3dA)

![Spot BMW - ¿Te gusta conducir?](https://i.makeagif.com/media/2-20-2018/CyYzhK.gif)



### Paper Display

**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

**b. Make a video of your paper display in action.**

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

### ✅ Part D
### Materiality

**Open Ended**: We are putting very few constraints on this part but we want you to get creative.

Design a system with the Pi and anything from your kit with a focus on form, and materiality. The "stuff" that enclose the system should be informed by the desired interaction.

**a. document the material prototype.** Include candidates that were considered even if they were set aside later.

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


**b. explain the selection.**

# Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design.

Reiterating:
### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


