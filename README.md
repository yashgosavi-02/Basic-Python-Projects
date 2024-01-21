# Basic-Python-Projects
## Weather App

A simple Python script to fetch and display the current weather of a specified city using the WeatherAPI. The user is prompted to input the city name, and the script retrieves temperature and weather conditions from the API, then uses text-to-speech to announce the information.

### Usage
1. Run `weatherApp.py`.
2. Enter the name of the city when prompted.

### Requirements
- Python 3.x
- Requests library (`pip install requests`)
- Pyttsx3 library (`pip install pyttsx3`)

---

## PDF Merger

A Python script to merge multiple PDF files into a single PDF file using PyPDF2 library. The script appends each PDF file to a PdfMerger object and then writes the merged content to a new PDF file.

### Usage
1. Add the PDF files you want to merge to the `pdfFiles` list in `pdfMerger.py`.
2. Run `pdfMerger.py`.

### Requirements
- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)

---

## Robo Speaker

A simple text-to-speech application that continuously prompts the user to input text. The program converts the input text into speech using the pyttsx3 library. The user can type "quit" to exit the program.

### Usage
1. Run `roboSpeaker.py`.
2. Enter text when prompted. Type "quit" to exit.

### Requirements
- Python 3.x
- Pyttsx3 library (`pip install pyttsx3`)

---

## Image Resizer

A Python script using OpenCV to resize an image based on configurable parameters. The source image is read, resized, and saved to a new destination with the desired scaling percentage.

### Usage
1. Replace the `source` and `destination` variables with the appropriate file paths in `imageResizer.py`.
2. Adjust the `scale_percent` variable if needed.
3. Run `imageResizer.py`.

### Requirements
- Python 3.x
- OpenCV library (`pip install opencv-python`)

---
