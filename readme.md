<!DOCTYPE html>
<html lang="en">
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rubik+Scribble&family=Syne:wght@400..800&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Rubik+Scribble&family=Syne:wght@400..800&display=swap" rel="stylesheet">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    


</head>
<body>

<h1 style="font-family: 'Outfit', sans-serif;">Virtual Mouse Using Hand Gesture Using OpenCV2</h1>

<p>This is a repository for a hand gesture recognition system implemented using MediaPipe for hand tracking and Flask for web streaming. The system captures video from the webcam, processes it to detect hand gestures in real-time, and displays the live feed along with recognized gestures on a web interface.</p>

<h2>Table of Contents</h2>

<div style="display: flex; gap: 10px; background-color: #f4f4f4; padding: 10px; justify-content: center;">
        <a href="#description" style="text-decoration: none; padding: 10px 20px; background-color: #007BFF; color: white; border-radius: 5px; font-weight: bold;">Description</a>
        <a href="#features" style="text-decoration: none; padding: 10px 20px; background-color: #fb5607; color: white; border-radius: 5px; font-weight: bold;">Features</a>
        <a href="#technologies-used" style="text-decoration: none; padding: 10px 20px; background-color: #ff006e; color: white; border-radius: 5px; font-weight: bold;">Technologies Used</a>
        <a href="#installation" style="text-decoration: none; padding: 10px 20px; background-color: #8338ec; color: white; border-radius: 5px; font-weight: bold;">Installation</a>
        <a href="#usage" style="text-decoration: none; padding: 10px 20px; background-color: #3a86ff; color: white; border-radius: 5px; font-weight: bold;">Usage</a>
    </div>


<h2 id="description">Description</h2>

<p>The system utilizes MediaPipe for hand tracking and gesture recognition, allowing users to control various functionalities using hand gestures. It's designed to be a flexible framework for integrating hand gesture recognition into interactive applications.</p>

<h2 id="features">Features</h2>

<ul>
  <li style="font-family: 'Outfit', sans-serif;">Real-time hand gesture recognition</li>
  <li style="font-family: 'Outfit', sans-serif;">Detection of various gestures including cursor movement, scrolling, clicking, dragging, etc.</li>
  <li style="font-family: 'Outfit', sans-serif;">Integration with Flask for web streaming</li>
  <li style="font-family: 'Outfit', sans-serif;">Adjustable cursor movement speed and volume control</li>
</ul>

<h2 id="technologies-used">Technologies Used</h2>

<ul>
  <li style="font-family: 'Outfit', sans-serif;"><img width="48" height="48" src="https://img.icons8.com/fluency/48/python.png" alt="python"/>Python</li>
  <li style="font-family: 'Outfit', sans-serif;"><img width="50" height="50" src="https://img.icons8.com/ios-filled/50/ffffff/flask.png" alt="flask"/>Flask</li>
  <li style="font-family: 'Outfit', sans-serif;"><img width="48" height="48" src="https://img.icons8.com/color/48/000000/opencv.png" alt="opencv"/>OpenCV</li>
  <li style="font-family: 'Outfit', sans-serif;"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLo4FAzwl7u7_1Ou16G_T421GjEwgcF61-fxOXh26F-SB_yrADoZRC6H_r-xwogH2V84I&usqp=CAU" width="50" height="50">MediaPipe</li>
</ul>

<h2 id="installation">Installation</h2>

<p>To run this project locally, follow these steps:</p>

<ol>
  <li style="font-family: 'Outfit', sans-serif;">Clone the repository: <code>git clone https://github.com/kovvurisuryavenkatareddy/virtual-mouse-using-hand-gesture.git</code></li>
  <li style="font-family: 'Outfit', sans-serif;">Navigate to the project directory: <code>cd main.py</code></li>
  <li style="font-family: 'Outfit', sans-serif;">Install required Python packages: <code>pip install flask opencv-python-headless mediapipe pyautogui</code></li>
  <li style="font-family: 'Outfit', sans-serif;">Run the Flask application: <code>python Main.py</code></li>
  <li style="font-family: 'Outfit', sans-serif;">Open your web browser and navigate to <code>http://127.0.0.1:5000/</code> to see the live hand tracking and recognized gestures.</li>
</ol>

<h2 id="usage">Usage</h2>

<p>This system can be used for various applications such as controlling presentations, interacting with virtual environments, or enhancing accessibility for users with mobility impairments. It provides a flexible framework for integrating hand gesture recognition into interactive systems and applications.</p>

</body>
</html>
