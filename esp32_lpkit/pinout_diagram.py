###########################################
#
# Example script to build a
# pinout diagram. Includes basic
# features and convenience classes.
#
###########################################

from pinout.core import Group, Image
from pinout.components.layout import Diagram
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components.legend import Legend


# Import data for the diagram
import data

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.
D_WIDTH = 1920
D_HEIGHT = 1080
diagram = Diagram(D_WIDTH, D_HEIGHT, "esp32_lpkit")


# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.add(Group())

# Add and embed an image
image = Image("esp32_lpkit.png", embed=True)
image.x = (diagram.width - image.width) // 2  # center the image\
image.y = 32 * 4
hardware = graphic.add(image)

# Measure and record key locations with the hardware Image instance
hardware.add_coord("3v3", 10, 81)
hardware.add_coord("gnd", 221, 79)
# Other (x,y) pairs can also be stored here
hardware.add_coord("pin_pitch_v", 0, 23)
hardware.add_coord("pin_pitch_h", 30, 0)
hardware.add_coord("usb_power", 112, 610)
hardware.add_coord("usup", 0, 476)
hardware.add_coord("bat", 230, 485)

# Create a single pin label
graphic.add(
    PinLabel(
        content="USB-POWER",
        x=hardware.coord("usb_power").x,
        y=hardware.coord("usb_power").y,
        tag="pwr",
        body={"x": 100, "y": 30, "width": 100, "height": 30},
        leaderline={"direction": "vh"},
    )
)


graphic.add(
    PinLabel(
        content="uSup i2c",
        x=hardware.coord("usup").x,
        y=hardware.coord("usup").y,
        tag="i2c",
        scale=(-1,1),
        body={"x": 30, "y": 0, "width": 100, "height": 30},
        leaderline=None,
    )
)

graphic.add(
    PinLabel(
        content="battery connector",
        x=hardware.coord("bat").x,
        y=hardware.coord("bat").y,
        tag="pwr",
        body={"x": 30, "y": 0, "width": 150, "height": 30},
        leaderline=None,
    )
)


# Create pinlabels on the right header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("gnd").x,
        y=hardware.coord("gnd").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(30, 0),
        label_pitch=(0, 23),
        labels=data.right_header,
        body={"height": 20, "width": 100},
    )
)


# Create pinlabels on the left header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("3v3").x,
        y=hardware.coord("3v3").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(30, 0),
        label_pitch=(0, 23),
        scale=(-1, 1),
        labels=data.left_header,
        body={"height": 20, "width": 100},
    )
)


# Title
title = TextBlock(data.title)
title.x = 16 * 3
title.y = 32 * 3
diagram.add(title)


# Create a legend
legend = Legend(data.legend)
legend.x = 32
legend.y = 32 * 8
diagram.add(legend)

with open("diagram.svg", "w") as f:
    f.write(diagram.render())
