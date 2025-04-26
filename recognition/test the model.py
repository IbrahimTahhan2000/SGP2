from os import close

from ultralytics import YOLO
import os
import cv2
from django.conf import settings

# model_path = os.path.join(settings.BASE_DIR, 'recognition/static/recognition/models/ASL.pt')
# print(os.getcwd().join('static/recognition/models/ASL.pt'))
model_path = os.path.dirname(__file__) + '/static/recognition/models/ASL.pt'
print(model_path + '\n\n')
# with open(model_path, 'rb') as f:
model = YOLO(model_path)

print(model.names)