<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Mouse Using Hand Gesture</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Outfit', sans-serif;
            text-align: center;
        }
        .btn-container {
            margin-top: 20px;
        }
        .btn {
            display: inline-block;
            margin: 10px;
        }
    </style>
</head>
<body>

    <h1>Virtual Mouse Using Hand Gesture Using OpenCV2</h1>

    <p>This is a repository for a hand gesture recognition system implemented using MediaPipe for hand tracking and Flask for web streaming. 
        The system captures video from the webcam, processes it to detect hand gestures in real-time, and displays the live feed along with 
        recognized gestures on a web interface.</p>

    <h2>Table of Contents</h2>

    <div class="btn-container">
        <a class="btn" href="#description"><img src="https://via.placeholder.com/150x50/ffbe0b/fff?text=Description" alt="Description"></a>
        <a class="btn" href="#features"><img src="https://via.placeholder.com/150x50/fb5607/fff?text=Features" alt="Features"></a>
        <a class="btn" href="#technologies-used"><img src="https://via.placeholder.com/150x50/ff006e/fff?text=Technologies_Used" alt="Technologies Used"></a>
        <a class="btn" href="#installation"><img src="https://via.placeholder.com/150x50/8338ec/fff?text=Installation" alt="Installation"></a>
        <a class="btn" href="#usage"><img src="https://via.placeholder.com/150x50/3a86ff/fff?text=Usage" alt="Usage"></a>
    </div>

    <h2 id="description">Description</h2>
    <p>The system utilizes MediaPipe for hand tracking and gesture recognition, allowing users to control various functionalities using hand gestures. 
        It's designed to be a flexible framework for integrating hand gesture recognition into interactive applications.</p>

    <h2 id="features">Features</h2>
    <ul>
        <li>Real-time hand gesture recognition</li>
        <li>Detection of various gestures including cursor movement, scrolling, clicking, dragging, etc.</li>
        <li>Integration with Flask for web streaming</li>
        <li>Adjustable cursor movement speed and volume control</li>
    </ul>

    <h2 id="technologies-used">Technologies Used</h2>
    <ul>
        <li><img width="48" height="48" src="https://img.icons8.com/fluency/48/python.png" alt="Python"/> Python</li>
        <li><img width="50" height="50" src="https://img.icons8.com/ios-filled/50/ffffff/flask.png" alt="Flask"/> Flask</li>
        <li><img width="48" height="48" src="https://img.icons8.com/color/48/000000/opencv.png" alt="OpenCV"/> OpenCV</li>
        <li><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLo4FAzwl7u7_1Ou16G_T421GjEwgcF61-fxOXh26F-SB_yrADoZRC6H_r-xwogH2V84I&usqp=CAU" width="50" height="50" alt="MediaPipe"> MediaPipe</li>
    </ul>

    <h2 id="installation">Installation</h2>
    <p>To run this project locally, follow these steps:</p>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/kovvurisuryavenkatareddy/virtual-mouse-using-hand-gesture.git</code></li>
        <li>Navigate to the project directory: <code>cd main.py</code></li>
        <li>Install required Python packages: <code>pip install flask opencv-python-headless mediapipe pyautogui</code></li>
        <li>Run the Flask application: <code>python Main.py</code></li>
        <li>Open your web browser and navigate to <code>http://127.0.0.1:5000/</code> to see the live hand tracking and recognized gestures.</li>
    </ol>

    <h2 id="usage">Usage</h2>
    <p>This system can be used for various applications such as controlling presentations, interacting with virtual environments, 
        or enhancing accessibility for users with mobility impairments. It provides a flexible framework for integrating hand gesture 
        recognition into interactive systems and applications.</p>

</body>
</html>
