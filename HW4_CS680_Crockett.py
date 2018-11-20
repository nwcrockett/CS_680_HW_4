"""
Nelson Crockett
CS 680 HW 4
20NOV18
nwcrockett@alaska.edu

This script will output the 
"""


import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")


last_color_change = cv2.getTickCount()
last_frame_black = True

sharp_brightness_level_change = False

previous_brightness_level = 0

while True:
    # read camera frame, change to gray scale, get mean of gray scale to obtain brightness levels
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness_level = gray.mean()

    # threshold in the if statement to find if a change in brightness has been detected
    if np.abs(brightness_level - previous_brightness_level) > 10:
        previous_brightness_level = brightness_level
        print("Last color change: " + str(last_color_change))
        last_color_change = cv2.getTickCount()

        if last_frame_black:
            # Last image was resulting from a dark screen. Output dark image
            gray[:] = 50
        else:
            gray[:] = 205

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
