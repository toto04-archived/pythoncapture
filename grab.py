import sys
import math
import numpy as np
from PIL import ImageGrab, Image
import os

nV = int(sys.argv[1])  # number of vertical leds
nH = int(sys.argv[2])  # number of horizontal leds

image = ImageGrab.grab()
w = image.width // (nH + 1)
h = image.height // (nV + 1)
colors = np.empty((nH + nV * 2, 3), dtype=np.uint8)

distance = 8

while 1:
    input()
    os.system('say hi')
    image = ImageGrab.grab()
    for n in range(0, nV):
        red = 0
        green = 0
        blue = 0
        yoff = image.height - (n * h + 3 * h // 2)
        for x in range(0, w, distance):
            for y in range(yoff, h + yoff, distance):
                pixel = image.getpixel((x, y))
                red += pixel[0]
                green += pixel[1]
                blue += pixel[2]
        ops = math.ceil(w / distance) * math.ceil(h / distance)
        red //= ops
        green //= ops
        blue //= ops
        colors[n] = [red, green, blue]
    for n in range(0, nH):
        red = 0
        green = 0
        blue = 0
        xoff = n * w + w // 2
        for x in range(xoff, w + xoff, distance):
            for y in range(0, h, distance):
                pixel = image.getpixel((x, y))
                red += pixel[0]
                green += pixel[1]
                blue += pixel[2]
        ops = math.ceil(w / distance) * math.ceil(h / distance)
        red //= ops
        green //= ops
        blue //= ops
        colors[n + nV] = [red, green, blue]
    for n in range(0, nV):
        red = 0
        green = 0
        blue = 0
        yoff = n * h + h // 2
        for x in range(image.width - w, image.width, distance):
            for y in range(yoff, h + yoff, distance):
                pixel = image.getpixel((x, y))
                red += pixel[0]
                green += pixel[1]
                blue += pixel[2]
        ops = math.ceil(w / distance) * math.ceil(h / distance)
        red //= ops
        green //= ops
        blue //= ops
        colors[n + nV + nH] = [red, green, blue]
    hexs = map(lambda color: ''.join(map(lambda x: hex(x)[2:], color)), colors)
    print(','.join(hexs))