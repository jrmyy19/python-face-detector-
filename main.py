import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Let the camera sensor physically initialize 
time.sleep(1.0) 

# Burn 20 frames to let auto-exposure adjust
for _ in range(20):
    cap.read()

print("Camera warmed up! Starting stream...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Webcam Live Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
