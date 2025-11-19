#Names
brdName = "esp32_lpkit" #add board name here
brdImgName = "esp32_lpkit.png" #add name of board .png


D_WIDTH = 1920 #resulting diagram width
D_HEIGHT = 1080 #resulting diagram height


#Hardware coordinates, add your hardware in the format ("name", x, y)
hwCoordiantes =[("3v3", 10, 81), ("3v3", 10, 81), ("gnd", 221, 79), ("pin_pitch_v", 0, 23), ("pin_pitch_h", 30, 0), ("usb_power", 112, 610), ("usup", 15, 476), ("bat", 230, 485)]


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

# Pinlabels. Each pin is an array of touples, with each touple being in the format of (TEXT, appearance)

left_header = [
    [
        ("3V3", "pwr"),
    ],
    [
        ("EN", "pwr"),
    ],
    [
        ("GP36", "gpio"),
        ("ADC1_0", "analog"),
        ("RTC_IO0", "rtc"),
        ("SENSOR_VP", "other"),
        ("INPUT ONLY", "other"),
    ],
    [
        ("GP39", "gpio"),
        ("ADC1_3", "analog"),
        ("RTC_IO3", "rtc"),
        ("SENSOR_VN", "other"),
        ("INPUT ONLY", "other"),
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
        ("ADC1_5", "analog"),
        ("RTC_IO8", "rtc"),
        ("Touch8", "other"),
        ("XTAL_32_N", "other"),
    ],
    [
        ("GP25", "gpio"),
        ("ADC2_8", "analog"),
        ("RTC_IO6", "rtc"),
        ("DAC1", "other"),
    ],
    [
        ("GP26", "gpio"),
        ("ADC2_9", "analog"),
        ("RTC_IO7", "rtc"),
        ("DAC2", "other"),
    ],
    [
        ("GP27", "gpio"),
        ("ADC2_7", "analog"),
        ("RTC_IO17", "rtc"),
        ("Touch7", "other"),
    ],
    [
        ("GP14", "gpio"),
        ("ADC2_6", "analog"),
        ("RTC_IO16", "rtc"),
        ("Touch6", "other"),
        ("HSPI_CLK", "spi"),
    ],
    [
        ("GP12", "gpio"),
        ("ADC2_5", "analog"),
        ("RTC_IO15", "rtc"),
        ("Touch5", "other"),
        ("HSPI_MISO", "spi"),
    ],
    [
        ("GND", "gnd"),
    ],
    [
        ("GP13", "gpio"),
        ("ADC2_4", "analog"),
        ("RTC_IO14", "rtc"),
        ("Touch4", "other"),
        ("HSPI_MOSI", "spi"),
    ],
    [
        ("VCC", "pwr"),
    ],
]


right_header = [
    [
        ("GND", "gnd"),
    ],
    [
        ("GP23", "gpio"),
        ("VSPI_MOSI", "spi"),
    ],
    [
        ("GP22", "gpio"),
        ("SCL", "i2c"),
    ],
    [
        ("GP1", "gpio"),
        ("TXD_0", "uart"),
    ],
    [
        ("GP3", "gpio"),
        ("RXD_0", "uart"),
    ],
    [
        ("GP21", "gpio"),
        ("I2C_SCL", "i2c"),
    ],
    [
        ("GND", "gnd"),
    ],
    [
        ("GP19", "gpio"),
        ("VSPI_MISO", "spi"),
    ],
    [
        ("GP18", "gpio"),
        ("VSPI_CLK", "spi"),
    ],
    [
        ("GP5", "gpio"),
        ("VSPI_CS0", "spi"),
    ],
    [
        ("GP17", "gpio"),
        ("TXD_2", "uart"),
    ],
    [
        ("GP16", "gpio"),
        ("RXD_2", "uart"),
    ],
    [
        ("GP4", "gpio"),
        ("ADC2_0", "adc"),
        ("RTC_IO10", "rtc"),
        ("Touch0", "other"),
    ],
    [
        ("GP0", "gpio"),
        ("ADC2_1", "adc"),
        ("RTC_IO11", "rtc"),
        ("Touch1", "other"),
    ],
    [
        ("GP2", "gpio"),
        ("ADC2_2", "adc"),
        ("RTC_IO12", "rtc"),
        ("Touch2", "other"),
    ],
    [
        ("GP15", "gpio"),
        ("ADC2_3", "adc"),
        ("RTC_IO13", "rtc"),
        ("Touch3", "other"),
        ("HSPI_CS0", "spi"),
    ],
]

def linear_search(data, target):
    for tup in data:
        if target in tup:
            return tup
    return None


#content, x, y, tag, scale, body, leaderline
#hwCoordiantes =[("3v3", 10, 81), ("3v3", 10, 81), ("gnd", 221, 79), ("pin_pitch_v", 0, 23), ("pin_pitch_h", 30, 0), ("usb_power", 112, 610), ("usup", 0, 476), ("bat", 230, 485)]
#linear_search(hwCoordiantes, "usb_power")
graphicPinLabels = [("USB-POWER", linear_search(hwCoordiantes, "usb_power")[1], linear_search(hwCoordiantes, "usb_power")[2], "pwr", (1, 1), {"x": 100, "y": 30, "width": 100, "height": 30}, {"direction": "vh"}),
                    ("uSup i2c", linear_search(hwCoordiantes, "usup")[1], linear_search(hwCoordiantes, "usup")[2], "i2c", (-1,1), {"x": 30, "y": 0, "width": 100, "height": 30}, None),
                    ("battery connector", linear_search(hwCoordiantes, "bat")[1], linear_search(hwCoordiantes, "bat")[2], "pwr", (1, 1), {"x": 30, "y": 0, "width": 150, "height": 30}, None)
    ]
graphicPinLabelGroups = [(linear_search(hwCoordiantes, "gnd")[1], linear_search(hwCoordiantes, "gnd")[2], linear_search(hwCoordiantes, "pin_pitch_v"), (30, 0), (0, 23), (1, 1), right_header, {"height": 20, "width": 100}),
                         (linear_search(hwCoordiantes, "3v3")[1], linear_search(hwCoordiantes, "3v3")[2], linear_search(hwCoordiantes, "pin_pitch_v"),(30, 0), (0, 23), (-1, 1), left_header, {"height": 20, "width": 100})
                         ]


# description = """Python tool kit to assist with
# documentation of electronic hardware.
# More info at <tspan class='italic strong'>pinout.readthedocs.io</tspan>"""


