import json
import sys
import swatch
from pinout.core import Group, Image
from pinout import config
from pinout.components.layout import Diagram
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components.legend import Legend, Swatch
from pinout.config import legend

def linear_search(data, target):
    for tup in data:
        if target in tup:
            return tup
    return None

def dict_search(arr, target):
    #val = next(item for item in arr if item["name"] == target)
    for dict in arr:
        if dict["name"] == target:
            return dict

# LOAD JSON FILE
dataFilepath = sys.argv[1] #import data as an argument
sys.path.insert(1, str(dataFilepath)) #insert filepath into python

with open(dataFilepath) as f: #open JSON
    data = json.load(f)

#IMPORT CSS
cssFilepath = ""

if data["customCssFilepath"]:
    cssFilepath = data["customCssFilepath"] # custom css
else:
    cssFilepath = "styles.css" # default css

diagram = Diagram(data["D_WIDTH"], data["D_HEIGHT"], data.brdName)

diagram.add_stylesheet(cssFilepath, embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.add(Group())

# Title
title = TextBlock(data["title"])
title.x = 16 * 3
title.y = 32 * 3
diagram.add(title)

# Add and embed an image
image = Image(data["brdImgName"], embed=True)
image.x = ((diagram.width - image.width) // 2) + 200 # center the image\
image.y = data["hgt_shift"]
hardware = graphic.add(image)

# Measure and record key locations with the hardware Image instance
for hw in data["hwCoordiantes"]:
    hardware.add_coord(["hwCoordiantes"]["name"], ["hwCoordiantes"]["x"], ["hwCoordiantes"]["y"])

# CREATE LEGENDS

config.legend["entry"]["height"] = 40
config.legend["entry"]["swatch"]["height"] = 10

legendNumber = 0

for legend in data["legendList"]:
    for item in data[legend]:
        legName = item["name"]
        legTag = item["tag"]
        legendX = data["legendCoords"][legendNumber]["x"]
        legendY = data["legendCoords"][legendNumber]["y"]

        legend = Legend(legend)
        legend.x = legendX + data["wid_shift"]
        legend.y = legendY + data["hgt_shift"]
        diagram.add(legend)

    legendNumber = legendNumber + 1

# CREATE TITLE

titleName = data["title"]
titleCode = "<tspan class='title strong'>", titleName ,"</tspan> <tspan class='title'>Pinout</tspan>"

# ADD HARDWARE COORDINATES

for record in data["hwCoordiantes"]:
    name = record["name"]
    recX = record["x"]
    recY = record["y"]
    # ADD CODE FOR ADDITIONS HERE

# ADD PIN LABELS AND PIN LABEL GROUPS

graphicPinLabels = []
graphicPinLabelGroups = []

# ADD PIN LABELS
for record in data["graphicPinLabelData"]: # Parse the data and add it to the array

    ## GET START COORDS
    start_Array = record["start_X"]["arr"]
    start_Searchterm = record["start_X"]["searchTerm"]
    start_dict = data[start_Array]
    hw_dict = dict_search(start_dict, start_Searchterm)
    X = hw_dict["x"] + data["wid_shift"]
    Y = hw_dict["y"] + data["hgt_shift"]

    ## GRAB DATA FROM THE RECORD
    pin = record["pin"]
    scale = record["scale"]
    tag = record["tag"]
    body = record["body"]
    leaderline = record["leaderline"]

    ## "ASSEMBLE" THE PIN DATA
    definedPin = [pin, X, Y, tag, scale, body, leaderline]
    graphicPinLabels.append(definedPin)

for Label in graphicPinLabels:
    graphic.add(PinLabel(
        content=Label[0],
        x=Label[1],
        y=Label[2],
        tag=Label[3],
        scale = Label[4],
        body=Label[5],
        leaderline=Label[7],
    )
)

# ADD PIN LABEL GROUPS

for record in data["graphicPinLabelGroupsData"]: # Parse the data and add it to the array

    ## GET START COORDS
    start_Array = record["start"]["arr"]
    start_Searchterm = record["start"]["searchTerm"]
    start_dict = data[start_Array]

    hw_dict = dict_search(start_dict, start_Searchterm)
    X = hw_dict["x"] + data["wid_shift"]
    Y = hw_dict["y"] + data["hgt_shift"]

    ## GET PIN PITCH
    start_Array = record["pinPitch"]["arr"]
    start_Searchterm = record["pinPitch"]["searchTerm"]
    start_dict = data[start_Array]

    hw_dict = dict_search(start_dict, start_Searchterm)
    pinPitch = hw_dict["y"]

    ## GRAB DATA FROM THE RECORD
    scale = record["scale"]
    label_start = record["label_start"]
    label_pitch = record["label_pitch"]
    name = record["name"] # Pin Group name
    size = record["size"]

    pinLabelGroup = (X, Y, pinPitch, (label_start["x"], label_start["y"]), (label_pitch["x"], label_pitch["y"]), (scale["x"], scale["y"]), name, size)
    graphicPinLabelGroups.append(pinLabelGroup)
    print(pinLabelGroup)

for Label in graphicPinLabelGroups:
    graphic.add(PinLabelGroup(
            x = Label[0],
            y = Label[1],
            pin_pitch = Label[2],
            label_start = Label[3],
            label_pitch = Label[4],
            scale = Label[5],
            labels = data[Label[6]],
            body = Label[7],
        )
    )

with open(dataFilepath + "/diagram.svg", "w") as f:
    f.write(diagram.render())