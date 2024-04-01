<h1 style="font-size: 36px; color: red;">Virtual Mouse Using Hand Gesture using OpenCV2</h1>

This is a repository for a hand gesture recognition system implemented using MediaPipe for hand tracking and Flask for web streaming. The system captures video from the webcam, processes it to detect hand gestures in real-time, and displays the live feed along with recognized gestures on a web interface.

## Table of Contents

[![Description](https://placehold.it/150x50/009955/fff?text=Description)](#description)
[![Features](https://placehold.it/150x50/0055ff/fff?text=Features)](#features)
[![Technologies Used](https://placehold.it/150x50/ff5500/fff?text=Technologies+Used)](#technologies-used)
[![Installation](https://placehold.it/150x50/aa00aa/fff?text=Installation)](#installation)
[![Usage](https://placehold.it/150x50/ff0000/fff?text=Usage)](#usage)

## Description

The system utilizes MediaPipe for hand tracking and gesture recognition, allowing users to control various functionalities using hand gestures. It's designed to be a flexible framework for integrating hand gesture recognition into interactive applications.

## Features

- Real-time hand gesture recognition
- Detection of various gestures including cursor movement, scrolling, clicking, dragging, etc.
- Integration with Flask for web streaming
- Adjustable cursor movement speed and volume control

## Technologies Used

- Python
- Flask
- OpenCV
- MediaPipe

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/kovvurisuryavenkatareddy/virtual-mouse-using-hand-gesture.git`
2. Navigate to the project directory: `cd main.py`
3. Install required Python packages: `pip install flask opencv-python-headless mediapipe pyautogui`
4. Run the Flask application: `python Main.py`
5. Open your web browser and navigate to `http://127.0.0.1:5000/` to see the live hand tracking and recognized gestures.

## Usage

This system can be used for various applications such as controlling presentations, interacting with virtual environments, or enhancing accessibility for users with mobility impairments. It provides a flexible framework for integrating hand gesture recognition into interactive systems and applications.
