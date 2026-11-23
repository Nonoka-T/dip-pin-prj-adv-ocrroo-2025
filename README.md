# Overview

Include a brief overview of the project, include:

- How do you deploy and run the project?
- What are its core dependencies?
- Who is it for and why?

## Requirements

- Tesseract OCR engine - `pytesseract` only calls the Tesseract program, Tesseract must be installed separately
  - macOS: `brew install tesseract`
  - other platforms: https://tesseract-ocr.github.io/tessdoc/Installation.html
  - Check if it's installed or not `tesseract --version`