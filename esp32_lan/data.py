#Names
brdName = "esplan" #add board name here
brdImgName = "esplan.png" #add name of board .png


D_WIDTH = 1920 #resulting diagram width
D_HEIGHT = 1200 #resulting diagram height


#Hardware coordinates, add your hardware in the format ("name", x, y)
hwCoordiantes =[("3v3", 303, 627), ("pin_pitch_v", 27, 0), ("pin_pitch_h", 0, 30), ("usb_power", 42, 506), ("usup", 240, 620)]


#certain labels don't generate properly, as the image gets moved by pinout_diagram.py. This calculates that same shift and allows it to be applied to pin labels
from pinout.core import Group, Image
image = Image(brdImgName, embed=True)
wid_shift = (D_WIDTH-image.width) // 2 #image.x
hgt_shift = 32 * 4 #image.y

# Text
title = "<tspan class='title strong'>LaskaKit ESP32-LPKit</tspan> <tspan class='title'>Pinout</tspan>"

legend = [
    ("Analog", "analog"),
    ("Other", "other"),
    ("Ground", "gnd"),
    ("GPIO", "gpio"),
    ("Power", "pwr"),
    ("RTC", "rtc"),
    ("I2C", "i2c"),
    ("SPI", "spi"),
    ("UART", "uart"),
]

# Pinlabels. Each header array is an array of pins. Each pin is an array of touples, with each touple being in the format of (TEXT, appearance)

header = [
    [
        ("3V3", "pwr"),
    ],
    [
        ("VCC", "pwr"),
    ],
    [
        ("GND", "gnd"),
    ],
    [
        ("GP34", "gpio"),
        ("ADC1_6", "analog"),
        ("RTC_IO4", "rtc"),
        ("INPUT ONLY", "other"),
    ],
    [
        ("GP35", "gpio"),
        ("ADC1_7", "analog"),
        ("RTC_IO5", "rtc"),
        ("INPUT ONLY", "other"),
    ],
    [
        ("GP32", "gpio"),
        ("ADC1_4", "analog"),
        ("RTC_IO9", "rtc"),
        ("Touch9", "other"),
        ("XTAL_32_P", "other"),
    ],
    [
        ("GP33", "gpio"),
        ("ADC1_4", "analog"),
        ("RTC_IO9", "rtc"),
        ("Touch9", "other"),
        ("XTAL_32_P", "other"),
    ],
    [
        ("GPO0", "gpio"),
        ("ADC1_5", "analog"),
        ("RTC_IO8", "rtc"),
        ("Touch8", "other"),
        ("XTAL_32_N", "other"),
    ],
    [
        ("TX1", "uart"),
    ],
    [
        ("GPO16", "gpio"),
        ("ADC2_8", "analog"),
        ("RTC_IO6", "rtc"),
        ("DAC1", "other"),
    ],
    [
        ("GPO13", "gpio"),
        ("ADC2_9", "analog"),
        ("RTC_IO7", "rtc"),
        ("DAC2", "other"),
    ],
    [
        ("GPO12", "gpio"),
        ("ADC2_7", "analog"),
        ("RTC_IO17", "rtc"),
        ("Touch7", "other"),
    ],
    [
        ("GPO14", "gpio"),
        ("ADC2_6", "analog"),
        ("RTC_IO16", "rtc"),
        ("Touch6", "other"),
        ("HSPI_CLK", "spi"),
    ],
    [
        ("SNS_VN", "gpio"),
    ],
    [
        ("RX1", "uart"),
    ],
    [
        ("EN", "pwr"),
    ],
]

def linear_search(data, target):
    for tup in data:
        if target in tup:
            return tup
    return None


#content
#x
#y
#tag
#scale
#body
#leaderline

graphicPinLabels = [("USB-POWER", linear_search(hwCoordiantes, "usb_power")[1], linear_search(hwCoordiantes, "usb_power")[2], "pwr", (1, 1), {"x": 100, "y": 30, "width": 100, "height": 30}, {"direction": "vh"}),
                    ("uSup i2c", linear_search(hwCoordiantes, "usup")[1], linear_search(hwCoordiantes, "usup")[2], "i2c", (-1,1), {"x": 100, "y": -30, "width": 100, "height": 30}, None),
    ]

#x, y: HW coordinates
#pin_pitch - space between pins
#label_start
#label_pitch
#scale - move this first one to change start of labels
#labels
#body

graphicPinLabelGroups = [(linear_search(hwCoordiantes, "3v3")[1], linear_search(hwCoordiantes, "3v3")[2], linear_search(hwCoordiantes, "pin_pitch_v"),(30, 40), (0, 23), (-1, 0.9), header, {"height": 20, "width": 100})
                         ]


# description = """Python tool kit to assist with
# documentation of electronic hardware.
# More info at <tspan class='italic strong'>pinout.readthedocs.io</tspan>"""


