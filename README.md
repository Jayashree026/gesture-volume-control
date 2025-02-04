Gesture-Based Volume Control

Overview:
This project allows you to control the system volume using hand gestures. It uses OpenCV, Mediapipe, and PyAutoGUI to detect the distance between the thumb and index finger, which is then mapped to volume control actions. The webcam feed is processed in real-time to adjust the volume.

Code Explanation
Libraries Used:
1. cv2 (OpenCV): Used for capturing video from the webcam and processing frames.
2. pyautogui: Simulates keyboard actions to control system volume (volume up/down).
3. mediapipe: Used for detecting and tracking hand landmarks (thumb and index finger tips).
4. math: To calculate the Euclidean distance between the thumb and index finger.
5. time: To manage timing for volume updates and prevent rapid changes.
   
Flow of the Code:
1. Initialize Mediapipe Hands:
        - The Mediapipe hands module detects hand landmarks and tracks the thumb and index finger tips.
        - The system uses min_detection_confidence and min_tracking_confidence to filter out unreliable hand detections.
2. Webcam Feed:
        - The webcam is initialized using OpenCV, and frames are captured continuously in a loop.
        - Each frame is flipped horizontally for a mirror effect to make it easier for the user to interact.
3. Hand Gesture Detection:
        - For each frame, the Mediapipe library detects hand landmarks. The thumb_tip and index_tip positions are then used for gesture recognition.
        - The normalized coordinates of these landmarks are converted to pixel values to calculate the Euclidean distance between the thumb and index finger.
4. Volume Control Logic:
        - The distance between the thumb and index finger is calculated.
        - A volume scale (0-100%) is derived from the distance, where a smaller distance means lower volume and a larger distance means higher volume.
        - The code adjusts the system volume using PyAutoGUI (volumedown and volumeup commands) based on the calculated volume. The update is limited to every 0.2 seconds to prevent excessive volume changes.
5. Display Volume:
        - The current volume percentage is displayed on the webcam feed in real-time.
6. Exit the Program:
        - Press 'q' to exit the webcam feed and stop the program.
   
How to Run
1. Install Dependencies:
        Before running the script, install the required Python libraries using:
                   pip install opencv-python pyautogui mediapipe (Command)
Run the Script:

2. Run the Python script:
        python gesture_volume_control.py (Command)
                - A webcam window will open, and the system volume will adjust based on the distance between your thumb and index finger.
   
Usage:
- Volume Up: Spread your thumb and index finger apart.
- Volume Down: Bring your thumb and index finger close together.
- The system will update the volume every 0.2 seconds for smoother control.
  
Exit:
To exit the application, press 'q'.
