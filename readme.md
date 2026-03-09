# How to use the LaskaKit Pinout Generator Script

## Preamble
Any code in this document will be pre-filled from the example ESPInk project. The template file will, however, be mostly empty other than for some universally necessary things.

1. You have a (preferrably otherwise empty) directory with 2 files:
    - A data.json file, the creation of which is described in the following chapter
    - An image of the board which you‘re annotating
2. For the program to run, you must install the pre-requisite python libraries, more on that in the How to run chapter. 

## Data JSON
This chapter describes the process of creating a functional data.json file for use with the current version of the pinout generator script.
## Basic information
The first part of the data.json is a section with basic information about the board.

```
"brdName": "ESPink", – Filename of the image to be edited
"brdImgName": "./espInk/ESPink.png", – Filepath from the directory where the script is located to where the image of the board is.
"D_WIDTH": 3180, - Width of the resulting diagram in pixels.
"D_HEIGHT": 1860, – Height of the resulting diagram in pixels.
  "_comment7": "wid_shift = ((D_WIDTH-image.width) // 2) + 200, in this case (3180-619)//2-200 = 2670",
"wid_shift": 1480, – By how much to shift the board Typically, the value can be derived from this formula: wid_shift = ((D_WIDTH-image.width) // 2) + 200, as seen in _comment7.
"hgt_shift": 128, – By how much to shift the board down.
"title": "LaskaKit ESP32-LPKit", – The tittle to be diplayed above the board
"customCssFilepath": null, – If you want to include custom CSS, add the filepath here, otherwise leave it as null.
"titleWidthShift": -430, – How much to shift the image to the right in pixels.
"titleHeightShift": 20, – How much to shift the image down in pixels.
```

### Legends
Each legend is made up of 3 parts – An array with legend entries, its name in the list, and coordinates. The template comes with 3 legends pre-made – One for uŠup I2C, one for uŠup SPI, and one to describe the colors of pin labels. 
It‘s important to note that the legend entries are an array of dictionaries, with each dictionary being one entry that contains some text as well as a tag, which determines the color of the example swatch which is displayed next to the text.

```
"legend": [
    {"label": "Analog", "tag": "analog"},
    {"label": "Other", "tag": "other"},
    {"label": "Ground", "tag": "gnd"},
    {"label": "GPIO", "tag": "gpio"},
    {"label": "Power", "tag": "pwr"},
    {"label": "RTC", "tag": "rtc"},
    {"label": "I2C", "tag": "i2c"},
    {"label": "SPI", "tag": "spi"},
    {"label": "UART", "tag": "uart"}
  ], – Basic legend with every color used for pin labels (- some used for things like uŠup SPI).
 
"legendSPI": [
    {"label": "CS - 46  ", "tag": "rtc"},
    {"label": "MOSI - 3 ", "tag": "mosi"},
    {"label": "SCK - 14 ", "tag": "scl"},
    {"label": "MISO - 21", "tag": "sda"},
    {"label": "3.3V - 47", "tag": "pwr"},
    {"label": "GND", "tag": "gnd"}
], – Legend for uŠup SPI for boards that use an ESP32S3. Change the pin number if you‘re describing a board with a different MCU.
 
"legendI2C": [
    {"label": "GND", "tag": "gnd"},
    {"label": "3.3V - 47", "tag": "pwr"},
    {"label": "SDA - 42", "tag": "sda"},
    {"label": "SCL - 2 ", "tag": "scl"}
], – Legend for uŠup for boards that use an ESP32S3. Change the pin number if you‘re describing a board with a different MCU.
 
"legendList": ["legendI2C", "legendSPI", "legend"], – List of all legends
"legendCoords": [{"x": -500, "y": 1075}, {"x": 850, "y": 550}, {"x": -1200, "y": 0}], – Coordinates for each legend in the order that they are listed above.
```

### Headers
Headers are sets of exposed pins, typically exposed with dupont pin–compatible holes or as pads (such as on the ESPLan board). 
Each header is defined by an array of arrays of dictionaries, where:
- Each array is one pin
- Each dictionary is one of the labels (the colorful rectangles with text) that is to be placed next to that pin. That dictionary contains 2 strings: A “label“ and a “tag“. The label being the text that is to be displayed within the rectangle, and the tag determining the rectangle‘s color.
    
```
"left_header": – Header definition
[ – Starting the header array
    [ – First pin 
        {"label": "3V3", "tag": "pwr"} – First label to be displayed next to the pin
    ],
    [ – Second pin 
        {"label": "EN", "tag": "pwr"}
    ],
    [ – Third pin. This pin has 4 labels next to it, unlike the previous two, which only had one each.
        {"label": "GPIO4", "tag": "gpio"},
        {"label": "ADC1 CH3", "tag": "analog"},
        {"label": "TOUCH 4", "tag": "other"},
        {"label": "RTC_IO4", "tag": "rtc"}
    ],
    Lines omitted...
    [
        {"label": "GND", "tag": "gnd"}
    ],
    [
        {"label": "VCC", "tag": "pwr"}
    ]
], – Ending the header array
```

### HW Coordinates
The “hwCoordinates“ array conains the coordinates for any and all important pins, namely:
- Pins that define the start of Pin Label Groups (typically the first pins on each pin header)
- USB, uŠup, and other connectors
- pin_pitch, which describes the pitch between pins on headers
The pin coordinates are taken from the BASE IMAGE.
    
```
"hwCoordiantes": [
    {"name": "3v3", "x": 50, "y": 143},
    {"name": "gnd", "x": 560, "y": 145},
    {"name": "pin_pitch", "x": 0, "y": 51},
    {"name": "usb_power", "x": 320, "y": 1435},
    {"name": "usup", "x": 80, "y": 1140},
    {"name": "bat", "x": 530, "y": 790},
    {"name": "disp", "x": 570, "y": 1150},
    {"name": "SPI", "x": 530, "y": 640}
],
```

### Pin Labels
Pin labels are used for annotating important hardware on the board.

```
"graphicPinLabelData": [
    {
        "pin": "USB-POWER", – Text to be displayed on the label
        "start_X": {"arr": "hwCoordiantes", "searchTerm": "usb_power"}, – name of the array where the start X coordinates are, usually HW coordinates + the name of the HW
        "start_Y": {"arr": "hwCoordiantes", "searcherm": "usb_power"},– name of the array where the start Y coordinates are, usually HW coordinates + the name of the HW
        "tag": "pwr", – tag to determine color of the label
        "scale": {"x": 1, "y": 1}, – determines the scale as well as the orientation of the tag, where changing the scale X or Y to a negative value will change where the line pointing to the board will come out of 
        "body": {"x": 0, "y": 200, "width": 300, "height": 40}, x/y move the label, width/height determine the size of the label
        "leaderline": {"direction": "vh"} – determines how the line point to the HW will look (options: hh, vh, hv, vv)
    },
    {
        "pin": "μŠup i2c",
        "start_X": {"arr": "hwCoordiantes", "searchTerm": "usup"},
        "start_Y": {"arr": "hwCoordiantes", "searchTerm": "usup"},
        "tag": "i2c",
        "scale": {"x": -1,"y": -1},
        "body": {"x": 100, "y": 0, "width": 200, "height": 40},
        "leaderline": null
    },
	...lines omitted...
    {
        "pin": "μŠup SPI",
        "start_X": {"arr": "hwCoordiantes", "searchTerm": "SPI", "index": 1},
        "start_Y": {"arr": "hwCoordiantes", "searchTerm": "SPI", "index": 2},
        "tag": "spi", "scale": {"x": 1, "y": 1},
        "body": {"x": 100, "y": 0, "width": 210, "height": 40},
        "leaderline": null
    }
],
```

### PinLabelGroups
Here is where we define how the pin label groups we defined earlier are generated. They defined very similarly to pin labels. 

```
"graphicPinLabelGroupsData": [
    {
        "start": {"arr": "hwCoordiantes", "searchTerm": "gnd"}, – name of array and term to search to find the first pin in the 							       group
        "pinPitch": {"arr": "hwCoordiantes", "searchTerm": "pin_pitch"}, – name of array and term to search to find the pin 								      pitch
        "label_start": {"x": 50, "y": 0}, – Where to move the first label in relation to the first pin
        "label_pitch": {"x": 0, "y": 50}, – Pitch between the labels
        "scale": {"x": 1, "y": 1}, – Same as pin labels
        "name": "right_header", – Name of the pin label group array 
        "size": {"height": 38, "width": 280} – Size of each pin label
    },
    {
        "start": {"arr": "hwCoordiantes", "searchTerm": "3v3"},
        "pinPitch": {"arr": "hwCoordiantes", "searchTerm": "pin_pitch_v"},
        "label_start": {"x": 50, "y": 0},
        "label_pitch": {"x": 0, "y": 50},
        "scale": {"x": -1, "y": 1},
        "name": "left_header",
        "size": {"height": 38, "width": 200}
    }
```

## Running the script
To make things as simple as possible, it‘s recommended to run the script through the uv command line tool.

First, install uv:

Fedora: ```sudo dnf install uv```
Ubuntu: ```sudo apt install uv```

After that create a virtual environment:

```uv venv```

Download and install dependencies:

```uv sync```

After that, you should be ready to go. You can launch the command by typing:

```uv run PinoutGenerator.py [path to data json]```


