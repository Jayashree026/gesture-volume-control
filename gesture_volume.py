import cv2
import pyautogui
import mediapipe as mp
import math
import time

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Track last volume change time
last_update_time = time.time()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with Mediapipe Hands
    results = hands.process(rgb_frame)
    
    # If landmarks are detected, draw them and control volume
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get the position of the thumb and index finger tips (for volume control)
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            # Convert normalized coordinates to pixel values
            h, w, _ = frame.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            
            # Calculate the Euclidean distance between thumb and index finger
            distance = math.sqrt((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2)
            
            # Normalize distance to a scale of 0 to 100 (adjust min/max values)
            min_dist = 20   # Distance when fingers are touching
            max_dist = 200  # Distance when fingers are wide apart
            
            volume = int(((distance - min_dist) / (max_dist - min_dist)) * 100)
            volume = min(max(volume, 0), 100)  # Clamp between 0 and 100
            
            # Adjust the volume only every 0.2 seconds for faster response
            current_time = time.time()
            if current_time - last_update_time > 0.2:  # Reduced delay from 0.5s to 0.2s
                if volume < 40:  
                    pyautogui.press('volumedown', presses=2)  # Faster decrease
                elif volume > 60:  
                    pyautogui.press('volumeup', presses=2)  # Faster increase
                
                last_update_time = current_time  # Update time
            
            # Display volume level on screen
            cv2.putText(frame, f'Volume: {volume}%', (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Gesture Volume Control", frame)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
