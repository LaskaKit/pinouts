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

# Pinlabels

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


# Text

title = "<tspan class='title strong'>LaskaKit ESP32-LPKit</tspan> <tspan class='title'>Pinout</tspan>"

# description = """Python tool kit to assist with
# documentation of electronic hardware.
# More info at <tspan class='italic strong'>pinout.readthedocs.io</tspan>"""
