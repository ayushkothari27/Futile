from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import dlib
import time
import math
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

vs = VideoStream(src=0).start()
time.sleep(1.0)

array_points_x = []
array_points_y = []
frame_no = -1
threshold_y = 100
threshold_x = 75

while True:
	frame_no = frame_no + 1
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 0)

	rect_1 = 0
	for (i, rect) in enumerate(rects):
		rect_1 = rect
		if not rect_1:
			continue
		break

	try:
		shape = predictor(gray, rect_1)
		shape = face_utils.shape_to_np(shape)

		points_x = []
		points_y = []
		for (x, y) in shape:
			cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
			if frame_no % 5 == 0:
				points_y.append(y)
				points_x.append(x)
		if frame_no % 5 == 0:
			array_points_x.append(points_x)
			array_points_y.append(points_y)
	except Exception as e:
		pass

	if frame_no%5==0 and frame_no!=0:
		dist_1_y = array_points_y[len(array_points_y)-1]
		dist_2_y = array_points_y[len(array_points_y)-2]
		dist_1_x = array_points_x[len(array_points_x)-1]
		dist_2_x = array_points_x[len(array_points_x)-2]
		sum_x = 0
		sum_y = 0
		for i in range(0,len(dist_2_y)):
			sum_y = sum_y + math.sqrt(abs(dist_1_y[i]*dist_1_y[i] - dist_2_y[i]*dist_2_y[i]))
			sum_x = sum_x + math.sqrt(abs(dist_1_x[i]*dist_1_x[i] - dist_2_x[i]*dist_2_x[i]))
		sum_y = sum_y /68
		sum_x = sum_x /68
		print(sum_y)
		print(sum_x)
		if sum_y>threshold_y and sum_x<threshold_x:
			cv2.putText(frame, "Head Nod detected!", (10, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()
