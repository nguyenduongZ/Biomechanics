import os
import csv
import glob
import math
import cv2
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose

# Setting up the Pose function.
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)

# Initializing mediapipe drawing class, useful for annotation.
mp_drawing = mp.solutions.drawing_utils 

# Data path
media_path = '/home/duong/3d/Biomechanics/sleep'

# Make csv_
csv_filename = 'landmarks_data.csv'

# Mở file CSV để ghi dữ liệu.
with open(csv_filename, mode='w', newline='') as csv_file:
    fieldnames = ['Image', 'Landmark_Name', 'Landmark_X', 'Landmark_Y', 'Landmark_Z', 'Visibility']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    # Lặp qua tất cả các tệp trong thư mục.
    for filename in os.listdir(media_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # Tạo đường dẫn đầy đủ đến tệp ảnh.
            image_path = os.path.join(media_path, filename)

            # Đọc tệp ảnh.
            sample_img = cv2.imread(image_path)
            image_rgb = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

            # Thực hiện pose detection sau khi chuyển ảnh sang định dạng RGB.
            results = pose.process(image_rgb)

            # Kiểm tra nếu có landmarks được tìm thấy.
            if results.pose_landmarks:
                for i, landmark in enumerate(results.pose_landmarks.landmark):
                    # Lấy chiều cao và chiều rộng của ảnh.
                    image_height, image_width, _ = sample_img.shape

                    # Ghi thông tin landmarks vào file CSV.
                    writer.writerow({
                        'Image': filename,
                        'Landmark_Name': mp_pose.PoseLandmark(i).name,
                        'Landmark_X': landmark.x,
                        'Landmark_Y': landmark.y,
                        'Landmark_Z': landmark.z if landmark.HasField('z') else None,
                        'Visibility': landmark.visibility
                    })

csv_dir = data_dir + "/landmarks_data.csv"