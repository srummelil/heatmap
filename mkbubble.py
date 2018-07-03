""" mkbubble.py creates an overlay image of bubbles for a heatmap.

Create an overlay image of filled circles with references to be placed on
top of a gradient to comprise a dynamically generated IT-Audit style heatmap.
Todo:
- Update to accept a list of points with coordinates and additional verbiage
and translate that list into bubbles.
- Allow users to specify format of bubbles?
"""

from PIL import Image, ImageDraw, ImageFont
import math
import random
import mkheatmap

xlim = 400
ylim = 400
diam = 30
rad = round(diam/2, 0)
ol = (255, 255, 255, 255)
fi = (0, 0, 255, 128)

points = [(random.randint(diam, xlim-diam),
           random.randint(diam, ylim-diam))
          for k in range(10)]

startletter = 97  # letter a
indicators = []
for letter in range(startletter, startletter + len(points)):
    indicators.append(chr(letter).upper())

textadj = round(math.sqrt(rad*rad/2), 0)
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf',
                         int(round(diam*.75, 0)))

# base = Image.open('out.jpg').convert('RGBA')
base = mkheatmap.makeimage(xlim, ylim).convert('RGBA')
# make a blank image for the text, initialized to transparent text color
overlay = Image.new('RGBA', base.size, (255, 255, 255, 0))
d = ImageDraw.Draw(overlay)

inc = 0  # Iterate through the indicators
for point in points:
    ubx, uby = point
    lbx = ubx + diam
    lby = uby + diam
    caption = str(indicators[inc] + str(inc))
    # caption = str(indicators[inc])
    # caption = str(inc)
    # For some reason, x seems skewed with only a signle character caption,
    # so needed to reduce the adjustment. Added conditional to make it
    # nice looking by default.
    if len(caption) < 2:
        textx = ubx + rad - (int(round(textadj/2, 0)))
    else:
        textx = ubx + rad - textadj
    texty = uby + rad - textadj

    d.ellipse([(ubx, uby), (lbx, lby)],
              fill=fi,
              outline=ol)
    d.text((textx, texty), caption, font=fnt, fill=ol)
    inc += 1

composited = Image.alpha_composite(base, overlay)
composited.show(title="Heatmap of Random Data", command=None)
