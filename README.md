

# How to run
- preferably use uv for its simplicity
- `uv run main.py`
- https://docs.astral.sh/uv/


# Requirements

## Basic principle
- there shall be one universal program that takes a board image and a json pinout definition as an input and outputs the pinout image in png format
- json pinout definition format is defined using jsonschema (pinout_shema.json)

## Directory structure
- each board shall have its own Directory
- in the directory there shall be an image of the board and a json definition on pinout

## Board image requirements
- image shall be exported from the pcb/cad
- image shall be scaled so the pin spacing is exactly 30px
- image shall have a transparent background
- image shall not contain any padding, all padding must be cropped
- image shell be in png or svg format
