# Overview

OCRroo is prototype that find and read the code shown in the videos.

# Who is it for and why?
Coding students who are blind or have low vision. Coding videos often show code on the screen,
but the narration usually doesn't read every detail so these students miss important information.
Turning the code on screen to text means it can be read by screen reader.

## Dependencies / Requirements
- [OpenCV](https://github.com/opencv/opencv-python) (`opencv-python`) - opens the video and gets frames
- [pytesseract](https://github.com/madmaze/pytesseract) - read the text in a frame (OCR) using the Tesseract engine
- Tesseract OCR engine - `pytesseract` only calls the Tesseract program, Tesseract must be installed separately
  - macOS: `brew install tesseract`
  - other platforms: https://tesseract-ocr.github.io/tessdoc/Installation.html
  - Check if it's installed or not `tesseract --version`
- [FastAPI](https://fastapi.tiangolo.com/) - provide a web API so other processes can use the OCR service

## How do you deploy and run the project?

1. Install `uv` and the Tesseract OCR engine
2. Install the Python dependencies: `uv sync`
3. Put test video in `resources/oop.mp4`
4. Try the library: `uv run python preliminary/library_basics.py`
5. Start API: `uv run fastapi dev preliminary/simple_api.py`
6. Call an endpoint like `curl 127.0.0.1:8000/video/demo/frame/42/ocr`