import cv2
import imutils

def motion_detection(frame, frame_check):
    	
    if frame_check is None:
    	# check background frame
    	frame_check = frame
		return frame_check
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	image = cv2.GaussianBlur(image, (21, 21), 0)
	# compute the absolute difference between the current frame and
	# first frame
	frameDelta = cv2.absdiff(frame_check, image)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < 30000:
			continue
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	return frame
	
	
