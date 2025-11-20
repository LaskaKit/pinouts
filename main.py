import json
import sys

import jsonschema

from pinout.components.layout import Diagram
from pinout.components.pinlabel import PinLabel, PinLabelGroup
from pinout.core import Group, Image

# load the pinout schema
with open("pinout_schema.json", "r") as f:
    schema = json.load(f)

# load the pinout definitions TODO: take the filepath as an argument
with open("esp32_lpkit/esp32_lpkit.json") as f:
    data = json.load(f)

# validate
try:
    jsonschema.validate(data, schema)
    print("Input data valid!", file=sys.stderr)
except jsonschema.ValidationError as e:
    print(f"Input data are not valid: {e}", file=sys.stderr)
    exit(1)


# data are valid -> we can continue
diagram = Diagram(data["width"], data["height"])
diagram.add_stylesheet("styles.css")

image = Image(data["image"])

graphic = diagram.add(Group())
graphic.x = 400  # this should be in the schema TODO
graphic.y = 50  # this should be in the schema TODO
graphic.add(image)

for group in data["pin_label_groups"]:
    pin_labels = [
        [
            PinLabel(
                content=label["name"],
                tag=label["tag"],
                scale=(group["scale"]["x"], group["scale"]["y"]),
            )
            for label in label_row
        ]
        for label_row in group["pin_label_rows"]
    ]
    pin_label_group = PinLabelGroup(
        x=group["pin_start"]["x"],
        y=group["pin_start"]["y"],
        scale=(group["scale"]["x"], group["scale"]["y"]),
        pin_pitch=(group["pin_pitch"]["x"], group["pin_pitch"]["y"]),
        label_start=(group["label_start"]["x"], group["label_start"]["y"]),
        label_pitch=(group["label_pitch"]["x"], group["label_pitch"]["y"]),
        labels=pin_labels,
    )
    graphic.add(pin_label_group)


# save the file
with open("tmp.svg", "w") as out:
    out.write(diagram.render())
