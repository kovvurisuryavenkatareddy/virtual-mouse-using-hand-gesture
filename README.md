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

<a href="#description"><img src="https://placehold.it/150x50/ffbe0b/fff?text=Description"></a>
<a href="#features"><img src="https://placehold.it/150x50/fb5607/fff?text=Features"></a>
<a href="#technologies-used"><img src="https://placehold.it/150x50/ff006e/fff?text=Technologies_Used"></a>
<a href="#installation"><img src="https://placehold.it/150x50/8338ec/fff?text=Installation"></a>
<a href="#usage"><img src="https://placehold.it/150x50/3a86ff/fff?text=Usage"></a>


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
  <li><img width="48" height="48" src="https://img.icons8.com/fluency/48/python.png" alt="python"/>Python</li>
  <li><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAADQElEQVR4nO3WfajeYxgH8N8ck7eJ5b2NyZCd7GReZi8IUxoyakRhWqwtL43kD2UaZm9m+Wf/UErmpZCXeTt/6FCkiDIxayIxCn+QP7x+dHmuc/p5PM95nhy1c3J/6+n53dd9/e7f/b3u6/ped1UVFBQUFBQUFBQU/O+AI7BPNdaBNViAPbv07+kwfwDuwA0j3NepeBbTu3HeFx/iEzzR6aU4ObyJ3/AWnsIb+A4fp8/N+AP3jIBED57UwKxuXpiHn/AoluWG7sPBHVIxcHHNdhCeqY2D5Mp/S6QWtAjIadVwwLH4Ht/gddyC89CHhRntiW1O8W9E0j6+9vzcSIkE8uQ7EomNrsX8/C3LtLg6iRyCKd0QwVlNPkHkruq/ITKrGyID+Cjz/DLskSc1f5j3BomsS8K3YX0LIkM1gv2wGo/hS1xZmzsSW/AiPsUFTURmYwZeyv0+jP3rH7sbv+AzXItpaT8Qc7ogsgnX4XGsaEFkVW0cKvZQPt+Jl2tz63FvPp+Aa1oQmZpE/5lmmJmOAym/M2tz53RBZEEt2pe0IPLX5prs47ER/TXbVbmPOK2pTf5hX4VvQ46Hk7h+7MjITsYZWS8LuyXSxieIrK6NezMlHkhZHTqRnJ+Ld/EzLm8ishmv4rW2PQy34kdswPPRR1L2+tp1+5TaTkRirXX5PA47I1g5vhGv1Hwvyv/d8CCero1/z+Aengq7sd0HI1LbsRVLcFQW/F44u01qrEwiL+D8Fj6Rz19g22DK4b38xv3Rb7I2N+XcO9mMl6foXJr2xfmdzRnYefleiNS5rciE+kj16s8N9mRRjmvy3R0n4RiciONbrDclPxp+vWmbEIHBYTk+enDtDNqMkPDB+bTH+ifnOoemrS+Lf1LVJoIRic9xBT7AmXH3qgvAmICGan2VpxLF/0im2CkRgWqsQCOVlqZyDGR+vx/9BIvqDWzUQyNXb8rO+0NqdxTixGiW2cWHGmU0J5xejUZoSOXyvA58nboe9XN72uNutiL7QXTa6+O0sg9dWI02aJzC3LxabMm62ZrkopYCv+bJvZ19Y0k1mqGhXtPyMtmbkhi1cxz23tX7KygoKCgoKCgoKCgoqHYR/gTgqPv2A6iVswAAAABJRU5ErkJggg==">Flask</li>
  <li><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAAElUlEQVR4nO2YzW8bRRjGN22TUAlaGuS1iVrg0BPXXJB6sOQZB0MECSQmTdQWiHfCh9QDf4FPKNkJqDKVkNLdCKTwUYwAceXCARSId1Kh8lGayG2TivbGoUGtQCIPGieY4t3XXsdg++BXmov3mdnfs/u+787YMDrRiU78Z4HDj+1HhJ1ClH0Kk1+HyX7fGRuIsk9K1x6O32O0Y8Dkk9ugHFWH1ph8wmiXgJHeC5O/VRPcZ4Tn9Nx2ePK5uuHLg51pLXyUje8efmfEEmOtgX803YMoLzZswGRXcTTV23wDJp+okt/rMNlwyeTRVC/MxEjpNzqVxlth4DzZZQ4P9vn0/eyBUmsNNvBB8w1E2WogTISNknNiyTTxFi63wADfDDYQv5ec05c6QBjYbEUK3Q6EeWjoEDlHp1Fw2v3WijdQrLcg6cJna82l34b5kGyLsVTEp4+lIjD5tfYp4hhZkLqNLvv0Jl8m9RG68P8/A8ZAN0x2hXiiUz59lE0RBoow4vuabmAbig8FAF2Akd3j0xrZPTB5wf+2EiMtgS+DmVzeBbSFSPIYqY0kj5U0/9TLbHNpg6AMowsmt8MWo9b8DQ/D6DLaJUrp1D94pKauf/AIYvzJ5lAZhpH9MrvPWck863pi0fGsH13P+lUPR4nvXWW9e86zhvP5NjiYBMVCQTzhKFF0lUCN8YVRRyRmMfb4DB6ppdMaJlF/iwWMLldZbzie2AoBD1dNp8Osm85jL5M4yyXAJT6updeaktZGLpuFr7OR4XhChgMXcJT1lTYcZt274LeHjTgJbyNeoc2Fgtc5HRbe9aw/nRVrIMy6SYn0v4AkwCS+02+lUqufNrOhKvU69areJLd6utfxxLXwBsR8GPiBeXQziauVQFxDSbxUqec2Xg7SMhsb6Sx6yBu5BTFaBXbtnGdNON9kou8svxpzC+LkwoUXfZu2oOASk0FAfDs1lgIMLFF6ZoM+frrKygfnuSg6SxnfMTFsMIl8IIzE2tAMfOcH/Zu+Rpg4TxvwxFqwgenndwtfMmDjCmFgtJ6a2RlF2oCy/ggyMK+mH2zEAJe4EwQTP4P7qTmDb6KPMHCHvJGjrNtBBha/PX2AmqPrgOhQ5XMul7gVBJPKgVyXz+IgYeAWacBV1npgCnkZcu/irGTGicIv/9PAbVwO7EBzOL6Lwv+ZNOB44iPiY3XR/Xrqvkr92xdfOUTVjatEeWfKbbxPdJQbyTmYlesmXkeU27hJzFmk30BBnKT7vnXJLYjjuo3Oq+mDzkrmKf2Uw2wv+Byeq9IWb3AbEzqddtJmkoKv+TGbV9PdjhIboT9ktNn1/A/pnooPGdUWUccoVv2QldJoJXOiYQMF4WuPSYlnGoK3scVtPF0VvmxCWQsNPH1y08UlZAMGZoy6DjFKuLuAP1vtcKM3adyGXe+TZxKzdW2ny29iJXPCUdbNWuCOJ37R7TTsugkbI2FqgkmsMolho5HIL72231XWC46yPneVuF465OhttBIbjrI+W/CsU3oXW++6urATsxjjEu8xG5e4xKYeTOIn3Sr1Na1pCL4TneiE0fbxF8QJuHsHQEMrAAAAAElFTkSuQmCC">OpenCV</li>
  <li><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLo4FAzwl7u7_1Ou16G_T421GjEwgcF61-fxOXh26F-SB_yrADoZRC6H_r-xwogH2V84I&usqp=CAU" width="50" height="50">MediaPipe</li>
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
