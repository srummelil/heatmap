# -*- coding: utf-8 -*-
"""
Purpose:
    Demonstrate creating a well-formatted heatmap in matplotlib.

Example:
    python heatmap_demo.py

Discussion:
    Author creates heatmaps for internal audit functions routinely.
    Doing so in MS Excel is awful, but common.
    This demo is a proof of concept to showcase Python and matplotlib
    capabilities for auto-generating graphical content and relieve
    the author from ever having to manually create a heatmap in MS Excel
    ever again.

Todo:
    Refine and post updates as applicable.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from mpl_toolkits.axes_grid1.colorbar import colorbar

# Create some random data
X = np.random.randn(1000)
Y = np.random.randn(1000)

# Round down and up to nearest integer for bottom and top of displayed range.
XMAX = math.ceil(X.max())
YMAX = math.ceil(Y.max())
XMIN = math.floor(X.min())
YMIN = math.floor(Y.min())

XEDGES = np.arange(XMIN, XMAX, 1)
YEDGES = np.arange(YMIN, YMAX, 1)

# Create our histogram.
HEATMAP, XEDGES, YEDGES = np.histogram2d(X, Y, bins=(XEDGES, YEDGES))

# Select a nice colorscheme. 'coolwarm' is good for risk ranking,
# as is 'plasma'.
# Possible colorschemes 'Purples', 'coolwarm', 'OrRd', 'hot',
# 'viridis', 'plasma'

CM = 'plasma'

HEATMAP_TITLE = 'Heatmap Title'
HEATMAP_XLABEL = 'Heatmap X Axis Label'
HEATMAP_YLABEL = 'Heatmap Y Axis Label'
LEGEND_YLABEL = 'Legend Y Axis Label'

# We are placing a single subplot on our plot.
# Alter the below to place multiple plots side by side
# or vertically. Add some whitespace for margin.
fig, (ax1) = plt.subplots(1)
fig.subplots_adjust(wspace=0.5)

# Set up our plot...
# Note, using the 'extent' argument with our edges arrays
# lets us dynamically size our heatmap.
plt.title(HEATMAP_TITLE)
plt.xlabel(HEATMAP_XLABEL)
plt.ylabel(HEATMAP_YLABEL)
# Note: I prefer 'blocky' heatmaps because I am usually
# dealing with a small population (<40 elements).
# You should consider your data population and alter the
# parameters accordingly. The below work well for risk assessments
# in which you will discuss the individual data points in detail
# with your audience.
im1 = plt.imshow(HEATMAP,
                 cmap=(CM),
                 interpolation='nearest',
                 origin='low',
                 extent=[XEDGES[0],
                         XEDGES[-1],
                         YEDGES[0],
                         YEDGES[-1]])

# We need to add a colorbar, so adding an axis to house it.
# This approach ensures our colorbar will be the same height as our
# plot and will dynamically resize with the plot.
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right",
                               size="7%",
                               pad="5%")

cb1 = colorbar(im1,
               cax=cax1
              )

cb1.ax.set_ylabel(LEGEND_YLABEL)

plt.show()
# To save file:
# plt.savefig('foo.png', bbox_inches='tight')
