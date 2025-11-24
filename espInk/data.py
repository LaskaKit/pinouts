#Names
brdName = "ESPink" #add board name here
brdImgName = "ESPink.png" #add name of board .png


D_WIDTH = 3180 #resulting diagram width
D_HEIGHT = 1860 #resulting diagram height


#certain labels don't generate properly, as the image gets moved by pinout_diagram.py. This calculates that same shift and allows it to be applied to pin labels
from pinout.core import Group, Image
image = Image(brdImgName, embed=True)
wid_shift = ((D_WIDTH-image.width) // 2) +200 #image.x
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



# Pinlabels. Each pin is an array of touples, with each touple being in the format of (TEXT, appearance)

left_header = [
    [
        ("3V3", "pwr"),
    ],
    [
        ("EN", "pwr"),
    ],
    [
        ("GP4", "gpio"),
        ("ADC1 CH3", "analog"),
        ("TOUCH 4", "other"),
        ("RTC_IO4", "rtc")
    ],
    [
        ("GP5", "gpio"),
        ("ADC1 CH4", "analog"),
        ("TOUCH 5", "other"),
        ("RTC_IO5", "rtc")
    ],
    [
        ("GP6", "gpio"),
        ("ADC1 CH5", "analog"),
        ("TOUCH 6", "other"),
        ("RTC_IO6", "rtc")
    ],
    [
        ("GP7", "gpio"),
        ("ADC1 CH6", "analog"),
        ("TOUCH 7", "other"),
        ("RTC_IO7", "rtc")
    ],
    [
        ("GP15", "gpio"),
        ("ADC2 CH4", "analog"),
        ("TOUCH 12", "other"),
        ("RTS_0", "spi"),
        ("RTC_IO15", "rtc"),
        ("RXD 1", "uart")
    ],
    [
        ("GP16", "gpio"),
        ("ADC2 CH5", "analog"),
        ("CTS_0", "spi"),
        ("RTC_IO16", "rtc"),
        ("TXD 1", "uart")
    ],
    [
        ("GP17", "gpio"),
        ("ADC2 CH6", "analog"),
        ("TXD 1", "spi"),
        ("RTC_IO17", "rtc")
    ],
    [
        ("GP18", "gpio"),
        ("ADC2 CH7", "analog"),
        ("RXD 1", "spi"),
        ("RTC_IO18", "rtc"),
        ("CLK_OUT3", "other")
    ],
    [
        ("GP8", "gpio"),
        ("ADC1 CH7", "analog"),
        ("TOUCH 8", "other"),
        ("RTC_IO8", "rtc"),
        ("SDA", "i2c")
    ],
    [
        ("GP19", "gpio"),
        ("ADC2 CH8", "analog"),
        ("RXD 2", "uart"),
        ("RTS 1", "spi"),
        ("RTC_IO19", "rtc"),
        ("CLK_OUT2", "other"),
        ("USB D+", "other")
    ],
    [
        ("GP20", "gpio"),
        ("ADC2 CH9", "analog"),
        ("TXD 2", "uart"),
        ("RTS 1", "spi"),
        ("RTC_IO19", "rtc"),
        ("CLK_OUT2", "other"),
        ("USB D-", "other")
    ],
    [
        ("GP3", "gpio"),
        ("ADC1 CH2", "analog"),
        ("TOUCH 3", "other"),
        ("RTC_IO3", "rtc"),
        ("JTAG", "other")
    ],
    [
        ("GND", "gnd"),
    ],
    [
        ("VCC", "pwr"),
    ]



]

right_header = [
    [
        ("GND", "gnd"),
    ],
    [
        ("GP1", "gpio"),
        ("ADC1 CH0", "analog"),
        ("TOUCH 1", "other"),
        ("RTC_IO1", "rtc"),
    ],
    [
        ("GP43", "gpio"),
        ("CLK OUT1", "other"),
        ("TXD 0","uart")
    ],
    [
        ("GP44", "gpio"),
        ("CLK OUT2", "other"),
        ("RXD 0", "uart")
    ],
    [
        ("GP41", "gpio"),
        ("MTDI", "other")
    ],
    [
        ("GP40", "gpio"),
        ("CLK OUT2", "other"),
        ("MTDO", "other")
    ],
    [
        ("GP39", "gpio"),
        ("CLK OUT3", "other"),
        ("MTDCK", "other")
    ],
    [
        ("GP38", "gpio"),
        ("FSPIPW", "other")
    ],
]

def linear_search(data, target):
    for tup in data:
        if target in tup:
            return tup
    return None


#Hardware coordinates, add your hardware in the format ("name", x, y)
hwCoordiantes =[("3v3", 50, 145), ("3v3", 10, 81), ("gnd", 560, 145), ("pin_pitch_v", 0, 51), ("pin_pitch_h", 50, 0), ("usb_power", 320, 1435), ("usup", 80, 1140), ("bat", 530, 790), ("disp", 570, 1150), ("SPI", 530, 640)]

#content, x, y, tag, scale, body, leaderline
#hwCoordiantes =[("3v3", 10, 81), ("3v3", 10, 81), ("gnd", 221, 79), ("pin_pitch_v", 0, 23), ("pin_pitch_h", 30, 0), ("usb_power", 112, 610), ("usup", 0, 476), ("bat", 230, 485)]
#linear_search(hwCoordiantes, "usb_power")
graphicPinLabels = [("USB-POWER", linear_search(hwCoordiantes, "usb_power")[1], linear_search(hwCoordiantes, "usb_power")[2], "pwr", (1, 1), {"x": 0, "y": 200, "width": 200, "height": 40}, {"direction": "vh"}),
                    ("uSup i2c", linear_search(hwCoordiantes, "usup")[1], linear_search(hwCoordiantes, "usup")[2], "i2c", (-1,1), {"x": 100, "y": 0, "width": 200, "height": 40}, None),
                    ("battery connector", linear_search(hwCoordiantes, "bat")[1], linear_search(hwCoordiantes, "bat")[2], "pwr", (1, 1), {"x": 100, "y": 0, "width": 250, "height": 40}, None),
                    ("Display Connector", linear_search(hwCoordiantes, "disp")[1], linear_search(hwCoordiantes, "disp")[2], "other", (1, 1), {"x": 100, "y": 0, "width": 300, "height": 40}, None),
                    ("uSup SPI", linear_search(hwCoordiantes, "SPI")[1], linear_search(hwCoordiantes, "SPI")[2], "i2c", (1, 1), {"x": 100, "y": 0, "width": 300, "height": 40}, None)

    ]
graphicPinLabelGroups = [(linear_search(hwCoordiantes, "gnd")[1], linear_search(hwCoordiantes, "gnd")[2], linear_search(hwCoordiantes, "pin_pitch_v"), (50, 0), (0, 50), (1, 1), right_header, {"height": 38, "width": 200}),
                         (linear_search(hwCoordiantes, "3v3")[1], linear_search(hwCoordiantes, "3v3")[2], linear_search(hwCoordiantes, "pin_pitch_v"),(50, 0), (0, 50), (-1, 1), left_header, {"height": 38, "width": 200})
                         ]


# description = """Python tool kit to assist with
# documentation of electronic hardware.
# More info at <tspan class='italic strong'>pinout.readthedocs.io</tspan>"""


