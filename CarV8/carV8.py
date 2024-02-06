import torch
from pathlib import Path
from PIL import Image
import cv2
import numpy as np


model = torch.hub.load('ultralytics/yolov5:master', 'yolov5s', pretrained=True)
video_path = 'CarV8/highway1.mp4'  # Change to your video file
cap = cv2.VideoCapture(video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to PIL Image
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    results = model(img)
    bboxes = results.xyxy[0].cpu().numpy()
    for bbox in bboxes:
        cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)

    cv2.imshow('Car Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
