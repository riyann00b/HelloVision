import cv2
import pyttsx3
import threading
import time
import platform

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed
engine.setProperty('voice', 'english')  # English voice

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Configuration Variables
GREETING_COOLDOWN = 5  # Cooldown for re-greeting (in seconds)
BOX_COLOR = (0, 255, 0)  # Color of the face rectangle
TEXT_COLOR = (255, 255, 255)  # Greeting text color
WINDOW_NAME = "Universal Face Detection"
greeted_faces = set()  # To track greeted faces

# Helper Functions
def speak_greeting():
    """Speak a greeting message."""
    engine.say("Hello! Nice to see you.")
    engine.runAndWait()

def draw_glowing_rectangle(frame, x, y, w, h, color=(0, 255, 0), thickness=2):
    """Draw a glowing rectangle around a detected face."""
    for i in range(1, 4):
        alpha = max(1 - 0.2 * i, 0)  # Fades the rectangle
        cv2.rectangle(frame, (x - i, y - i), (x + w + i, y + h + i), color, thickness)
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness * 2)

def detect_os_and_set_backend():
    """Detect operating system and configure backend."""
    os_name = platform.system().lower()
    if os_name == "linux":
        return cv2.CAP_V4L2  # Linux-specific backend
    elif os_name == "windows":
        return cv2.CAP_DSHOW  # Windows-specific backend
    else:
        return 0  # Default backend for other OS

def main():
    global greeted_faces
    video_backend = detect_os_and_set_backend()
    cap = cv2.VideoCapture(0, video_backend)  # Auto-configured for OS
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    # Create GUI window
    cv2.namedWindow(WINDOW_NAME)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from camera.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        # Check each detected face
        current_faces = set()
        for (x, y, w, h) in faces:
            # Generate unique face ID based on position
            face_id = (x // 10, y // 10)  # Scale down for consistency
            current_faces.add(face_id)

            # Greet once per face while visible
            if face_id not in greeted_faces:
                greeted_faces.add(face_id)
                threading.Thread(target=speak_greeting).start()

            # Draw glowing rectangle and text
            draw_glowing_rectangle(frame, x, y, w, h, color=BOX_COLOR)
            cv2.putText(frame, "Hello!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, TEXT_COLOR, 2)

        # Cleanup: Remove faces no longer visible
        greeted_faces.intersection_update(current_faces)

        # Show frame
        cv2.imshow(WINDOW_NAME, frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
