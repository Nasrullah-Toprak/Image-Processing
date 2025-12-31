# Webcam ROI Grayscale

This program uses OpenCV to read live video from a webcam and convert
a small region in the center of the image to grayscale.

## What it does
- Opens the default camera
- Reads video frames continuously
- Finds the center of the frame
- Selects a 200x200 pixel region (ROI) at the center
- Converts only that region to grayscale
- Shows the result in real time
- Closes when the 'q' key is pressed

## Requirements
- Python 3
- OpenCV

Install OpenCV:
pip install opencv-python

## How to run
python roi_grayscale.py

## Controls
- Press 'q' to quit the program

## Notes
- Only the center area is converted to grayscale
- The rest of the image stays in color
