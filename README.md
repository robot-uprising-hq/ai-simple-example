> [!WARNING]
> This repository has not been updated since late 2020 and may need old versions of dependencies or extensive modifications in order to work.

There's also a community built simulator, [Zero Ones Simulated](https://github.com/zero-ones-given/zero-ones-simulated), that can be used as a starting point for an environment for ML training, although integration with Unity ML Agents is not provided out of the box at least yet.

# AI Simple Example

Read the summary of Micro Invaders from [here](https://github.com/robot-uprising-hq/ai-guide).

This repo has example code showing how to get started with:

1. Detecting energy cores from an image by color
1. Detecting aruco markers from an image
1. Sending move commands to the robot

## Installation

### Prequisites

- git
- python3 & python3-pip & virtualen

- Webcam or Raspberry Pi Camera module
- Gstreamer (if you use Raspberry Pi Camera module)

- Robot's firmware [ai-robot-udp](https://github.com/robot-uprising-hq/ai-robot-udp)

### Downloading the files

The following works on Ubuntu and Mac.

Download and install this repo and its Python dependencies using the installation scripts in [AI Guide repo](https://github.com/robot-uprising-hq/ai-guide).

You can also use the following commands to do the same. Note that using virtual environment to isolate the Python environment is not mandatory but considered as a good practise.

```sh
git clone https://github.com/robot-uprising-hq/ai-simple-example.git
cd ai-simple-example
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

### Aruco marker detection

The `detect_aruco_markers_from_image.py` script shows how to detect 4x4 type Aruco Markers from an image and get their positions and rotations in the image.

1. Set the `VIDEO_SOURCE`-variable to `ffmpeg`, `gstreamer` or `webcam` depending on which one you use for video source.
1. Run `python detect_aruco_markers_from_image.py`

### Energy core detection

The `detect_energy_cores_from_image.py` script shows how to detect colored objects from the image and get their positions in the image.

1. Set the `VIDEO_SOURCE`-variable to `ffmpeg`, `gstreamer`, `webcam` depending on which one you use for video source.
1. Set the `POS_ECORE_LOW_COLOR`, `POS_ECORE_HIGH_COLOR`, `NEG_ECORE_LOW_COLOR`, `NEG_ECORE_HIGH_COLOR`-variables to the correct values in HSV-colorspace. See the comments in the script to understand how to choose the HSV low and high values.
1. Run `python detect_energy_cores_from_image.py`

### Move Robot

The `move_robot.py` script assumes that you have installed [ai-robot-udp](https://github.com/robot-uprising-hq/ai-robot-udp) firmware into your robot.
1. Put power on to the robot and find it's IP address
1. Set proper values to the variables `ROBOT_IP` and `ROBOT_PORT`
1. Run `python move_robot.py`

---

## Notes for different video sources
### FFmpeg video source
OpenCV can parse a MJPEG video stream with it's FFmpeg library.

When starting to read the video stream the FFmpeg library will print the following warning messages. If your PC is low performance you might get these and other warnings during the streaming.
```sh
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
[rtp @ 0x1a90a80] Received packet without a start chunk; dropping frame.
```

### Gstreamer video source
Gstreamer is a bit hard to set to Windows so it might be better to use the `ffmpeg` or `webcam` options.

To use the `gstreamer_video_source.py` as video stream you need to install Gstreamer to your PC and link the `gi`-package to your virtual environment. You can make the installation and create the symbolic link with the `install-gstreamer.sh`-script.

```sh
chmod +x install-gstreamer.sh
./install-gstreamer.sh
```

If you use Raspberry Pi camera module to as the video source see the [AI Video Streamer Repo](https://github.com/robot-uprising-hq/ai-video-streamer) for how to set it up.
