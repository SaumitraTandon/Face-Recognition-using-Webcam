# Real-Time Face Recognition using OpenCV and face_recognition

This repository contains two Python scripts that demonstrate real-time face recognition using different approaches: Local Binary Pattern Histogram (LBPH) and face_recognition library.

## Prerequisites

- Python 3.x
- OpenCV library
- face_recognition library (for `Face Recognition using Webcam.py`)

## Installation

1. Clone the repository:
2. Install the required dependencies:
3. Download the required files:
- `haarcascade_frontalface_default.xml` (for face detection)
- `lbph_classifier.yml` (pre-trained LBPH classifier for `camera_lbph.py`)
- `Saumitra.jpg` (sample image for `Face Recognition using Webcam.py`)

Place these files in the repository directory.

## Usage

### 1. camera_lbph.py

This script uses the LBPH algorithm for face recognition.

1. Connect a webcam or a camera to your computer.
2. Run the script:
The script will open a window displaying the real-time video feed from the connected camera. Recognized faces will be displayed with their names and confidence scores.

To exit the script, press the 'q' key.

### 2. Face Recognition using Webcam.py

This script uses the face_recognition library for face recognition.

1. Connect a webcam or a camera to your computer.
2. Run the script:
The script will open a window displaying the real-time video feed from the connected camera. Recognized faces will be displayed with their names.

To exit the script, press the 'q' key.

## File Structure

- `camera_lbph.py`: Python script for real-time face recognition using LBPH.
- `Face Recognition using Webcam.py`: Python script for real-time face recognition using face_recognition library.
- `haarcascade_frontalface_default.xml`: Haar cascade classifier for face detection.
- `lbph_classifier.yml`: Pre-trained LBPH classifier for `camera_lbph.py`.
- `Saumitra.jpg`: Sample image for `Face Recognition using Webcam.py`.
- `README.md`: This file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- The OpenCV library and its contributors.
- The face_recognition library and its contributors.
- The Haar cascade classifier and pre-trained LBPH classifier used in this project.
