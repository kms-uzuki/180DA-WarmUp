import numpy as np
import matplotlib
import cv2
# import random

image = cv2.VideoCapture(0)

while (1):
	retval, img = image.read()
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# define range of blue color in HSV
	# randnum_lower = random.randint(0,350)
	# randnum_upper = randnum_lower + 1
	# if randnum_upper > 349:
	# 	randnum_lower = 349

	lower = np.array([50,50,50])
	upper = np.array([150,205,205])

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
