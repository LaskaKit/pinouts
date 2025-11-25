###########################################
#
# Example script to build a
# pinout diagram. Includes basic
# features and convenience classes.
#
###########################################
import swatch
from pinout.core import Group, Image
from pinout import config
from pinout.components.layout import Diagram
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components.legend import Legend, Swatch
from pinout.config import legend
#import cv2

# Import data for the diagram
import data
from data import brdImgName

# Read image data UNUSED - READING IMAGE DATA UNNECESSARY.
# img = cv2.imread(brdImgName)

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.


D_WIDTH = data.D_WIDTH
D_HEIGHT = data.D_HEIGHT

diagram = Diagram(D_WIDTH, D_HEIGHT, data.brdName)


# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.add(Group())

# Add and embed an image
image = Image(data.brdImgName, embed=True)
image.x = ((diagram.width - image.width) // 2) + 200 # center the image\
image.y = 32 * 4
hardware = graphic.add(image)

# Measure and record key locations with the hardware Image instance
for name, x, y in data.hwCoordiantes:
    hardware.add_coord(name, x, y)


for content, x, y, tag, scale, body, leaderline in data.graphicPinLabels:
    graphic.add(PinLabel(
        content=content,
        x=x + data.wid_shift,
        y=y + data.hgt_shift,
        tag=tag,
        scale = scale,
        body=body,
        leaderline=leaderline,
    )
)

for x, y, pin_pitch, label_start, label_pitch, scale, labels, body in data.graphicPinLabelGroups:
    graphic.add(
        PinLabelGroup(
            x = x + data.wid_shift,
            y = y + data.hgt_shift,
            pin_pitch = (hardware.coord("pin_pitch_v", raw=True)),
            label_start = label_start,
            label_pitch = label_pitch,
            scale = scale,
            labels = labels,
            body = body,
        )
    )

# Title
title = TextBlock(data.title)
title.x = 16 * 3
title.y = 32 * 3
diagram.add(title)

config.legend["entry"]["height"] = 40
config.legend["entry"]["swatch"]["height"] = 10


# Create a legend
#legend = Legend(data.legend)
#legend.x = 32
#legend.y = 32 * 8
#legend.skewx = 200
#diagram.add(legend)

# Create legends

for leg, loc in zip(data.legendList, data.legendCoords):
    legend = Legend(leg)
    legend.x = loc[0] + data.wid_shift
    legend.y = loc[1] + data.hgt_shift
    diagram.add(legend)



with open("diagram.svg", "w") as f:
    f.write(diagram.render())

