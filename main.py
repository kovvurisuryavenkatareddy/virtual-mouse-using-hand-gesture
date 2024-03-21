from flask import Flask, render_template, Response
import cv2  # Import OpenCV for image and video processing
import mediapipe as mp  # Import MediaPipe library for hand tracking
from controller import GestureManager  # Import GestureManager class from controller module

app = Flask(__name__)  # Initialize Flask application

manager = GestureManager()  # Create an instance of the GestureManager class

mp_hands = mp.solutions.hands  # Initialize MediaPipe Hands module
mp_draw = mp.solutions.drawing_utils  # Initialize MediaPipe drawing utilities

hands = mp_hands.Hands()  # Create a Hands object for hand detection

cap = cv2.VideoCapture(0)  # Initialize video capture from the default webcam (index 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set the frame width to 640 pixels
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set the frame height to 480 pixels
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # Disable autofocus

@app.route('/')  # Define a route for the root URL
def index():
    
    return render_template('index.html')  # Render the index.html template when accessing the root URL

def generate_frames():
    while True:  # Loop indefinitely
        ret, frame = cap.read()  # Read a frame from the video capture
        if not ret:  # If frame cannot be captured, exit the loop
            break
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame from BGR to RGB
        results = hands.process(rgbFrame)  # Process the frame to detect hand landmarks using MediaPipe

        if results.multi_hand_landmarks:  # If hand landmarks are detected
            if len(results.multi_hand_landmarks) == 1:  # If only one hand is detected
                manager.hand_Landmarks = results.multi_hand_landmarks[0]  # Update the hand landmarks in GestureManager
            mp_draw.draw_landmarks(frame, manager.hand_Landmarks, mp_hands.HAND_CONNECTIONS)  # Draw hand landmarks on the frame
            manager.update_fingers_status()  # Update the status of finger positions
            manager.cursor_moving()  # Move the cursor based on hand position
            manager.detect_scrolling()  # Detect scrolling gesture
            manager.detect_zoomming()  # Detect zooming gesture
            manager.detect_clicking()  # Detect clicking gesture
            manager.detect_dragging()  # Detect dragging gesture
            manager.adjust_volume()  # Adjust volume based on hand gesture
            manager.take_screenshot_if_three_fingers_up()  # Take screenshot if three fingers are up

        ret, buffer = cv2.imencode('.jpg', frame)  # Encode the frame into JPEG format
        frame = buffer.tobytes()  # Convert the frame to bytes
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Yield the frame as a multipart response

@app.route('/video_feed')  # Define a route for streaming video feed
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')  # Return streaming response with generated frames

if __name__ == '__main__':  # Check if the script is executed directly
    app.run(debug=True)  # Start the Flask application in debug mode
