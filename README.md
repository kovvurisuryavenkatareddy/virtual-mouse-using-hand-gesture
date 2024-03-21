<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hand Gesture Recognition using MediaPipe and Flask</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #f8f8f8;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        p {
            line-height: 1.6;
            color: #555;
        }
        code {
            background-color: #f0f0f0;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: Consolas, monospace;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hand Gesture Recognition using MediaPipe and Flask</h1>
        <p>This project implements hand gesture recognition using MediaPipe for hand tracking and Flask for web streaming. The system captures video from the webcam, processes it to detect hand gestures in real-time, and displays the live feed along with recognized gestures on a web interface.</p>
        
        <h2>Prerequisites</h2>
        <ul>
            <li>Python 3.x installed on your system</li>
            <li>Install required Python packages using pip:</li>
        </ul>
        <code>pip install flask opencv-python-headless mediapipe pyautogui</code>
        
        <h2>Usage</h2>
        <ol>
            <li>Clone the repository:</li>
            <code>git clone &lt;repository_url&gt;</code>
            <li>Navigate to the project directory:</li>
            <code>cd &lt;project_directory&gt;</code>
            <li>Run the Flask application:</li>
            <code>python Main.py</code>
            <li>Open your web browser and navigate to <code>http://127.0.0.1:5000/</code> to see the live hand tracking and recognized gestures.</li>
        </ol>
        
        <h2>Files</h2>
        <ul>
            <li><strong>Main.py</strong>: This script initializes the Flask application, sets up video capture from the webcam, and integrates hand tracking and gesture recognition using MediaPipe.</li>
            <li><strong>controller.py</strong>: This module contains the <code>GestureManager</code> class, responsible for managing hand gestures, cursor movement, scrolling, zooming, clicking, dragging, volume adjustment, and screenshot capture based on detected hand landmarks.</li>
            <li><strong>index.html</strong>: This HTML template file defines the structure of the web interface. It displays the live video feed along with recognized hand gestures.</li>
        </ul>
        
        <!-- Other sections like Features, Dependencies, Acknowledgments, License can be added here -->
    </div>
</body>
</html>
