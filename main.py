import ultralytics
from ultralytics import YOLO
import supervision
import torch
import cv2
from collections import defaultdict
import supervision as sv

# Load a pretrained YOLOv8n model
model = ultralytics.YOLO('yolov8n.pt')

# with open 