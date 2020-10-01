import cv2
from gstreamer_video_source import GStreamerVideoSource


def select_video_source(selection):
    if selection == 'gstreamer':
        image_source = GStreamerVideoSource()

        def get_image():
            return image_source.frame()
        return get_image
    elif selection == 'webcam':
        cap = cv2.VideoCapture(0)

        def get_image():
            ret, frame = cap.read()
            return frame
        return get_image
    else:
        raise Exception("Unknown video source")
