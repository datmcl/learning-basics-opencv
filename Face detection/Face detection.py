import os
import cv2
from mtcnn import MTCNN
import numpy as np

def main(source):
    # Creating detector
    detector = MTCNN()

    # Starting video capture frame by frame from chosen source
    videoCapture = cv2.VideoCapture(0) if source == '0' else cv2.VideoCapture(source)

    while True:
        # Selecting a frame from the video
        _, frame = videoCapture.read()
        detections = detector.detect_faces(frame)

        # Minimal confidence to detect
        min_conf = 0.95

        # Drawing a rectangle at detected face
        for det in detections:
            if det['confidence'] >= min_conf:
                x, y, width, height = det['box']
                keypoints = det['keypoints']
                cv2.rectangle(frame, (x,y), (x+width,y+height), (190, 0, 95), 2)

        # Some info
        cv2.putText(frame, f'People on video: {len(detections)}', (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,155,255), 3)   
        cv2.putText(frame, 'Press Q to exit', (0,700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,155,255), 3)

        cv2.imshow('Face detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    videoCapture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Enter 0 to capture from webcam or enter source of video like this:\n\n/path/to/your/video.mp4\n\nEnter Q to exit...\n")

    # Source choosing
    while True:
        source = input()
        if source == '0':
            main(source)
            break
        elif os.path.isfile(source) == True:
            main(source)
            break
        
        # Validation
        exit(0) if source == 'Q' or source == 'q' else print('Enter again...')            
 