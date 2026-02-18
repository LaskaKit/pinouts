# First we import all the necessary libraries

import json
import sys
from pinout.core import Group, Image
from pinout import config
from pinout.components.layout import Diagram
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components.legend import Legend, Swatch
from pinout.config import legend

#Linear search, currently unused.
# def linear_search(data, target):
#     for tup in data:
#         if target in tup:
#             return tup
#     return None

# My implementation of linear dictionary search
def dict_search(arr, target):
    for dict in arr: # Searches through an array of dictionaries
        if dict["name"] == target: # If an attribute "name" matches the target argument
            return dict # It returns the dictionary

# Turns an Array of dictionaries (with the attributes "label" and "tag") into an array of touples
# Necessary as most functions from pinout don't accept dictionaries as inputs
def arrOfDictsToArrOfTups(dict):
    tuplist = []
    for entry in dict:
        tuplist.append((entry["label"], entry["tag"]))
    return tuplist

# Used for turning preparing PinLabelGroupsData for Use
# Turn an array of arrays of Dictionaries into an array of arrays of Touples
def arrOfArrsOfDictsToArrOfArrsOfTups(list):
    tuplist = []
    for listinlistoftuplists in list:
        tuplist.append(arrOfDictsToArrOfTups(listinlistoftuplists))
    return tuplist

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

#Set up the diagram page
diagram = Diagram(data["D_WIDTH"], data["D_HEIGHT"], data["brdName"])

#Add the CSS stylesheet
diagram.add_stylesheet(cssFilepath, embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.add(Group())

# Add and embed an image
image = Image(data["brdImgName"], embed=True)
image.x = ((diagram.width - image.width) // 2) + 200 # center the image\
image.y = data["hgt_shift"]
hardware = graphic.add(image)

# CREATE TITLE
titleName = data["title"]
titleCode = (
    f"<tspan class='title strong'>{data['title']}</tspan> "
    f"<tspan class='title'>Pinout</tspan>"
)

title = TextBlock(titleCode)
title.x = ((diagram.width + (image.width // 2)) // 2) + data["titleWidthShift"] # center the image
title.y = data["hgt_shift"] // 2 + data["titleHeightShift"] # Put the title slightly above the board
diagram.add(title)

# Measure and record key locations with the hardware Image instance
for hw in data["hwCoordiantes"]:
    hardware.add_coord(hw["name"], hw["x"], hw["y"])

# CREATE LEGENDS
config.legend["entry"]["height"] = 30
config.legend["entry"]["swatch"]["height"] = 18
config.legend["entry"]["swatch"]["width"] = 60

legendNumber = 0

for legend in data["legendList"]: #Iterate over the list of legends

    #Prepare the legend for future use
    temporaryLegendStorage = arrOfDictsToArrOfTups(data[legend])

    #ACTUALLY CREATE LEGEND
    singular_legend = Legend(temporaryLegendStorage)

    #Grab the coordinates
    legend_X = data["legendCoords"][legendNumber]["x"] + data["wid_shift"]
    legend_Y = data["legendCoords"][legendNumber]["y"] + data["hgt_shift"]

    singular_legend.x = legend_X
    singular_legend.y = legend_Y

    #Ddd the legedend to the diagram
    diagram.add(singular_legend)

    legendNumber = legendNumber + 1

# ADD HARDWARE COORDINATES

for record in data["hwCoordiantes"]:
     name = record["name"]
     recX = record["x"]
     recY = record["y"]
     hardware.add_coord(name, recX, recY)

# ADD PIN LABELS AND PIN LABEL GROUPS

graphicPinLabels = []
graphicPinLabelGroups = []

config.pinlabel["body"].update({"width": 3000})

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
    scale = (record["scale"]["x"], record["scale"]["x"])
    tag = record["tag"]
    body = record["body"]
    leaderline = record["leaderline"]

    ## "ASSEMBLE" THE PIN DATA
    definedPin = [pin, X, Y, tag, scale, body, leaderline]
    graphicPinLabels.append(definedPin)

# Finally actually add the lables
for Label in graphicPinLabels:
    graphic.add(PinLabel(
        content=Label[0],
        x=Label[1],
        y=Label[2],
        tag=Label[3],
        scale = Label[4],
        body=Label[5],
        leaderline=Label[6],
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

    # Data prepared, assemble and add it to the array
    pinLabelGroup = (X, Y, pinPitch, (label_start["x"], label_start["y"]), (label_pitch["x"], label_pitch["y"]), (scale["x"], scale["y"]), name, size)
    graphicPinLabelGroups.append(pinLabelGroup)

#Add pin label groups to the image
for Label in graphicPinLabelGroups:
    labels = arrOfArrsOfDictsToArrOfArrsOfTups(data[Label[6]])
    graphic.add(
        PinLabelGroup(
            x = Label[0],
            y = Label[1],
            pin_pitch = (hardware.coord("pin_pitch", raw=True)),
            label_start = Label[3],
            label_pitch = Label[4],
            scale = Label[5],
            labels = labels,
            body = Label[7],
        )
    )

# Create a filepath for the image, assume it's in the same folder as the .json
imgFilepath = dataFilepath.replace("/data.json", "/diagram.svg")

# Render the image
with open(imgFilepath, "w") as f:
    f.write(diagram.render())