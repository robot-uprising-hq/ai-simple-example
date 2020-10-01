# AI Simple Example

Read the summary of Micro Invaders from [here](https://github.com/robot-uprising-hq/ai-guide).

This repo has example code showing how to get started with:
1. Detecting energy cores from an image by color
1. Detecting aruco markers from an image
1. Sending move commands to the robot

# Installation

## Prequisites

- python3
- Git
- Webcam or Raspberry Pi Camera module

## Downloading the files

Download and install this repo and its Python dependencies using the installation scripts in [AI Guide repo](https://github.com/robot-uprising-hq/ai-guide)

# Usage
## Aruco marker detection
The `detect_aruco_markers_from_image.py` script shows how to detect 4x4 type Aruco Markers from an image and get their positions and rotations in the image.

1. Set the `VIDEO_SOURCE`-variable to `gstreamer` or `webcam` depending on which one you use for video source.
1. Run `python detect_aruco_markers_from_image.py`


## Energy core detection
The `detect_energy_cores_from_image.py` script shows how to detect colored objects from the image and get their positions in the image.

1. Set the `VIDEO_SOURCE`-variable to `gstreamer` or `webcam` depending on which one you use for video source.
1. Set the `POS_ECORE_LOW_COLOR`, `POS_ECORE_HIGH_COLOR`, `NEG_ECORE_LOW_COLOR`, `NEG_ECORE_HIGH_COLOR`-variables to the correct values in HSV-colorspace. See the comments in the script to understand how to choose the HSV low and high values.
1. Run `python detect_energy_cores_from_image.py`

## Using Gstreamer video source
If you use Raspberry Pi camera module to as the video source see the [AI Video Streamer Repo](https://github.com/robot-uprising-hq/ai-video-streamer) for how to set it up.