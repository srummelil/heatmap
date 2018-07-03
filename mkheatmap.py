#!/usr/bin/python
"""Create an image of the prescribed size in pixels and scale a heatmap.

Heatmap should appear as follows:
background - green in the lower left, red in the upper right,
fading to yellow in the middle.
To be used as a backround for audit-risk style heatmaps
(e.g., likelihood vs impact).
The RGB values for the colors:
        RED  GREEN  BLUE
Yellow  255, 255,   0
Green     0, 255,   0
Yellow  255, 255,   0
Red     255, 0,     0
Also, need to scale red and green down y axis
pixels[column, row] = (R, G, B)
for each line, calclate the left and right colors
left side is yellow to green so:
toprow = 255, 255, 0 to 255, 0, 0
toprow - 1 = (255 - rscale, 255, 0) to (255, rscale, 0)
and then paint between them.

Todo:
- Add ability to specify output image format and filename
- Add ability to choose whether to show, display, etc. image
"""

from PIL import Image


def makeimage(rows, cols):
    """Make the image itself."""
    r, c = rows, cols
    img = Image.new('RGB', (c, r), "black")
    pixels = img.load()

    CLRMAX = 255
    CLRMIN = 0

    rscale = int(round(CLRMAX / r, 0))
    cscale = int(round(CLRMAX / c, 0))
    red = CLRMAX
    green = CLRMAX
    blue = CLRMIN  # Never changes for this heatmap.

    for row in range(r):
        for col in range(c):
            cred = red - (rscale * row) + (cscale * col)
            cgreen = green + (rscale * row) - (cscale * col)
            pixels[col, row] = (cred, cgreen, blue)
    return img


if __name__ == '__main__':
    img = makeimage(255, 255)
    img.show()
