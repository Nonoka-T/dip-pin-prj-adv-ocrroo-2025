"""A basic introduction to Open CV

Instructions
------------

Implement the functions below based on their docstrings.

Notice some docstrings include references to third-party documentation
Some docstrings **require** you to add references to third-party documentation.

Make sure you read the docstrings C.A.R.E.F.U.L.Y (yes, I took the L to check that you are awake!)
"""

# imports - add all required imports here
from pathlib import Path
import cv2
import numpy as np
import pytesseract


VID_PATH = Path("resources/oop.mp4")

class CodingVideo:
    """Open coding video and give access to frame and metadata"""
    capture: cv2.VideoCapture


    def __init__(self, video: Path | str):
        """open the video file and read basic metadata"""
        #open video file
        self.capture = cv2.VideoCapture(str(video))
        if not self.capture.isOpened():
            raise ValueError(f"Cannot open {video}")

        #frame per second and read from video's property
        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        #total number of frame, convert to int from float
        self.frame_count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        # total length of video in seconds
        self.duration = self.frame_count / self.fps


    def __str__(self) -> str:
        """Displays key metadata from the video

        Specifically, the following information is shown:
            FPS - Number of frames per second rounded to two decimal points
            FRAME COUNT - The total number of frames in the video
            DURATION (minutes) - Calculated total duration of the video given FPS and FRAME COUNT

        Reference
        ----------
        https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        """
        #round fps to two decimal point
        fps_text = f"FPS: {round(self.fps, 2)}"
        frame_count_text = f"Frame Count: {self.frame_count}"
        #self duration in second so divide by 60 to get in minutes
        duration_text = f"Duration: {round(self.duration / 60, 2)} minutes"
        #show each value on own line
        return fps_text + "\n" + frame_count_text + "\n" + duration_text

    def get_frame_number_at_time(self, seconds: int) -> int:
        """Given a time in seconds, returns the value of the nearest frame"""
        #frame per second x second = frame number, round to the nearest whole frame
        return round(seconds * self.fps)


    def get_frame_rgb_array(self, frame_number: int) -> np.ndarray:
        """Returns a numpy N-dimensional array (ndarray)

        The array represents the RGB values of each pixel in a given frame

        Note: cv2 defaults to BGR format, so this function converts the color space to RGB

        Reference
        ---------
        https://docs.opencv.org/5.0/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html

        """
        #move the video to requested frame
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        #read that frame ok is true if it worked, frame is the image(BGR order)
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")
        # change the colour order from BGR opencv default fo RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return rgb_frame

    def get_image_as_bytes(self, seconds: int) -> bytes:
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.get_frame_number_at_time(seconds))
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")
        ok, buf = cv2.imencode(".png", frame)
        if not ok:
            raise ValueError("Failed to encode frame")
        return buf.tobytes()




    def save_as_image(self, seconds: int, output_path: Path | str = 'output.png') -> None:
        """Saves the given frame as a png image
        use OpenCV (third party library), cv2.imwrite convert the ndarray to png file.

        Reference
        ---------
        https://docs.opencv.org/5.0/main_modules/imgcodecs.html

        """
        # move the video to the frame closest ti the given time
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.get_frame_number_at_time(seconds))
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")
        saved = cv2.imwrite(output_path, frame)
        if not saved:
            raise ValueError(f"Failed to save image to {output_path}")

    def get_text_at_time(self, seconds: int) -> str:
        """
        return the text show in the video at the given time
        Use pytesseract (python wrapper for Tesseract OCR) - image_to_string reads the text in an image.
        It accepts Numpy array and expect RGB, so frame comes from get_frame_rgb_array.

        Reference
        ---------
        https://github.com/madmaze/pytesseract/blob/master/README.rst
        """
        frame_number = self.get_frame_number_at_time(seconds)
        rgb_frame = self.get_frame_rgb_array(frame_number)
        text = pytesseract.image_to_string(rgb_frame)
        return text

def test():
    """Try out your class here"""
    oop = CodingVideo("resources/oop.mp4")
    print(oop)
    oop.save_as_image(42)
    print(oop.get_text_at_time(42))

if __name__ == '__main__':
    test()