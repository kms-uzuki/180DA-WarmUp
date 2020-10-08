#!/usr/bin/env

import numpy as np
import matplotlib
import cv2
# import random

def nothing(x):
	pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 180, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 180, 180, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


#img = cv2.imread("hummbird.png", cv2.IMREAD_REDUCED_COLOR_2)
image = cv2.VideoCapture(0)


while (1):
	retval, img = image.read()
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# openCV uses scale to 179 for hue and 255 for saturation/luminance 

	l_h = cv2.getTrackbarPos("LH", "Tracking")
	l_s = cv2.getTrackbarPos("LS", "Tracking")
	l_v = cv2.getTrackbarPos("LV", "Tracking")

	u_h = cv2.getTrackbarPos("UH", "Tracking")
	u_s = cv2.getTrackbarPos("US", "Tracking")
	u_v = cv2.getTrackbarPos("UV", "Tracking")

	lower = np.array([l_h, l_s, l_v])
	upper = np.array([u_h, u_s, u_v])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower, upper)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(img,img, mask= mask)

	cv2.imshow('frame',img)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	k = cv2.waitKey(50) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()
