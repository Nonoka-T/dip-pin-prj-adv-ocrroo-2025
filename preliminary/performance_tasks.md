# Overview
This section contains preliminary familiarisation steps with the core libraries of the project. It is also designed to complement (and satisfy) the performance requirements of the preliminary assessment.

## Required performance demonstration

You must demonstrate your ability at:

- Determining an organisation’s technology, development tools, and UI platform
- Enabling interprocess communication in Python while using third-party libraries and referencing third-party documentation


## Instructions

1. Complete the knowledge section (Word document) available via Blackboard
2. Fork this repository
3. Clone the repository to your local computer
4. Install `uv` and check that it is running with `uv --version`
5. Obtain a video that can be used to test the functionality and place in the `resources/` folder - your instructor will provide you with one
6. Follow the steps in the remainder of the guide insuring your commit to git whenever prompted
7. Submit a `zip` of this repository along with the `.git` folder. **Do not include your `venv/`**. Ensure your submission includes the assessment Word document with all of the questions in it attempted.


## Steps
Complete the steps below and fill in the `> block` sections
> If you see a section like this, fill it in!


### Installing and running OpenCV

1. Examine the `pyproject.toml` what dependencies does it currently identify?
>None. the dependencies list is empty (dependencies=[]).
> File only set the project name and the version with the minimum python version.
>
2. Create a `.venv` in this folder using `uv venv`
3. Activate the `venv` as instructed by `uv`
4. In order to complete the project, we need to install OpenCV. Fill in the following:
  - What role does OpenCV have in this project?
  > OpenCV open the coding video and jump to given time or frame and reads that frame as image.
  > we can save the frame as PNG or pass it to tesseract so the code screen can be read as text.
  > 

  - What is the `uv pip` command to install OpenCV?
  > `uv pip install opencv-python`
  - What is the URL of this library's git repo?
  > [Insert URL Here](https://github.com/opencv/opencv-python)
5. Add OpenCV to your project using the `uv add` command:
  > `uv add name-of-open-cv-library

6. Have the dependencies in the `pyproject.toml` changed? If so, how?
  > changed to "opencv-python>=5.0.0.93".
  > uv alo created "uv.lock" that records the exact version installed.
7. Why did we use `uv add` over `uv pip`?
  > uv pip only install th package into the current venv like normal pip and not record it anywhere.
  > uv add installs it and save it in pyproject.toml and uv.lock so anyone who clone the repo can run "uv sync"
  > and get same package
  >
8. The `numpy` library is required for OpenCV. Should you add an explicit requirement for it? Why/Why not?
  > numpy is dependency of opencv-python so uv installs it automatically and records the exact version in uv.lock.
  > Our code only use numpy for the arrays that OpenCV returns so OpenCV decide which numpy version is compatible
  > Adding ourselves could cause a version conflict.
  >
9. Commit the changes so far to git. Use the message `chore: add OpenCV dependency`
10. Go to `preliminary/library_basics.py` and complete the required functionality.
11. Commit your changes with `feat: save video frames`


### Installing and running Tesseract

[Tesseract OCR](https://github.com/tesseract-ocr/tesseract) provides optical character recognition (OCR) functionality needed for the project.

Tesseract consists of both an OCR Engine and a command line program. It is predominantly written in C++.

1. Examine the [Readme](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file) and find a list of Python wrappers.

2. What is the URL that lists Python wrappers for Tesseract?
  > <url-here> https://tesseract-ocr.github.io/tessdoc/AddOns.html#tesseract-wrappers

3. Select a Python wrapper. What wrapper did you choose and why? Ensure you address each element below in your answer
> name of the python library
> - pytesseract (https://github.com/madmaze/pytesseract)

> how long ago was a commit made to the library
> - Last commit was on 18th Feb 2025

> does it have external dependencies
> - It needs python packages Pillow and packaging (uv installs these automatically),
> and the Tesseract OCR engine must be installed separately on the computer (on mac: `brew install tesseract`).

> how does it suite the project requirement
> - It is simple to use with on function `image_to_string()`, return the text in an image.
> It accepts a NumPy array so frame from `CodingVideo.get_frame_rgb_array()` can be passed straight in.
> - README shoe this in "Support for OpenCV image/NumPy array objects"

4. Use UV to add the dependency to your project and your `pyproject.toml`

5. If your library has additional requirements (e.g. installing tesseract binaries), note it in your README.md

6. Commit the new dependency `chore: add tesseract dependency`

7. Add a new method in `library_basics.py` that returns the text of a given frame/time/image (you decide!)

8. Commit the changes as `feat: OCR an image


### Install and run FastAPI

FastAPI will allow us to enable communication with our OCR service from other processes on the current machine or across a network.

1. Add the requirement for FastAPI using UV. FastAPI has optional requirements so the command is a little different:
`uv add fastapi --extra standard`
2. Commit the new dependency `chore: add FastAPI dependency`
3. Run in development mode using:
`uv run fastapi dev preliminary/simple_api.py`
4. Run the following curl command (may require git bash on Windows):
`curl 127.0.0.1:8000/video`
5. Confirm that a list of videos and URLs is returned by copying the output below:
> Description
6. What are the names of the two processes that just communicated?
>
6. Modify the simple_api.py so that it works correctly with your implementation and complete any TODO markers
7. Demonstrate the use of at least two other end points below:
>
>
>