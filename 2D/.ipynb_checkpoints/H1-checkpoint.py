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

def detectPose(image, pose, display=True):
    
    # Create a copy of the input image.
    output_image = image.copy()
    
    # Convert the image from BGR into RGB format.
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Perform the Pose Detection.
    results = pose.process(imageRGB)
    
    # Retrieve the height and width of the input image.
    height, width, _ = image.shape
    
    # Initialize a list to store the detected landmarks.
    landmarks = []
    
    # Check if any landmarks are detected.
    if results.pose_landmarks:
    
        # Draw Pose landmarks on the output image.
        mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):
            lst = []
            n = 0
            lst[n] = lst.append([id, lm.x, lm.y])
            n+1
            h, w, c = image.shape
             # Lấy tọa độ chân
            if id == 32 or id == 31:
                cx1, cy1 = int(lm.x * w), int(lm.y * h)
                cv2.circle(image, (cx1, cy1), 15, (0, 0, 0), cv2.FILLED)
                #tính chiều cao
                d = ((cx2 - cx1) ** 2 + (cy2 - cy1) ** 2) ** 0.5
                print(d)
                di = round(d * 0.5)
                print(di)
                cv2.putText(image, "Height : ", (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), thickness=2)
                cv2.putText(image, str(di), (180, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), thickness=2)
                cv2.putText(image, "cms", (240, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), thickness=2)
            # Lấy tọa độ lông mày
            if id == 6:
                cx2, cy2 = int(lm.x * w), int(lm.y * h)
                cy2 = cy2 + 20
                cv2.circle(image, (cx2, cy2), 15, (0, 0, 0), cv2.FILLED)
                
        # Iterate over the detected landmarks.
        for landmark in results.pose_landmarks.landmark:
            
            # Append the landmark into the list.
            landmarks.append((int(landmark.x * width), int(landmark.y * height),
                                  (landmark.z * width)))
    
    # Check if the original input image and the resultant image are specified to be displayed.
    if display:
    
        # Display the original input image and the resultant image.
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');
        
        # Also Plot the Pose landmarks in 3D.
        # mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

    
    # Otherwise
    else:
        
        # Return the output image and the found landmarks.
        return output_image, landmarks    