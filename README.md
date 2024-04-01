<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Virtual Mouse Using Hand Gesture Using OpenCV2</h1>

<p>This is a repository for a hand gesture recognition system implemented using MediaPipe for hand tracking and Flask for web streaming. The system captures video from the webcam, processes it to detect hand gestures in real-time, and displays the live feed along with recognized gestures on a web interface.</p>

<h2>Table of Contents</h2>

<a href="#description" style="font-size: large;"><img src="https://placehold.it/150x50/ffbe0b/fff?text=Description"></a>
<a href="#features" style="font-size: small;"><img src="https://placehold.it/150x50/fb5607/fff?text=Features"></a>
<a href="#technologies-used" style="font-size: small;"><img src="https://placehold.it/150x50/ff006e/000?text=Technologies_Used"></a>
<a href="#installation" style="font-size: small;"><img src="https://placehold.it/150x50/8338ec/fff?text=Installation"></a>
<a href="#usage" style="font-size: small;"><img src="https://placehold.it/150x50/3a86ff/fff?text=Usage"></a>


<h2 id="description">Description</h2>

<p>The system utilizes MediaPipe for hand tracking and gesture recognition, allowing users to control various functionalities using hand gestures. It's designed to be a flexible framework for integrating hand gesture recognition into interactive applications.</p>

<h2 id="features">Features</h2>

<ul>
  <li>Real-time hand gesture recognition</li>
  <li>Detection of various gestures including cursor movement, scrolling, clicking, dragging, etc.</li>
  <li>Integration with Flask for web streaming</li>
  <li>Adjustable cursor movement speed and volume control</li>
</ul>

<h2 id="technologies-used">Technologies Used</h2>

<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
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

<p>This system can be used for various applications such as controlling presentations, interacting with virtual environments, or enhancing accessibility for users with mobility impairments. It provides a flexible framework for integrating hand gesture recognition into interactive systems and applications.</p>

</body>
</html>
