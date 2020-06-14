import cv2
import sys
import motion_detection
from load_track import load_model
from main_tracker import track


def detection():

    # read video
    cap = cv2.VideoCapture(sys.argv[1])

    # Define the codec and create VideoWriter object
    ret, frame = cap.read()
    height , width , layers =  frame.shape
    
    #define output video
    video_output = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'),
                          cap.get(cv2.cv.CV_CAP_PROP_FPS), (width,height))
    
    #load model for tracker
    tracker, encoder = load_model()
    frame_check = None

    while ret:
        frame, boxs = motion_detection(frame, frame_check)
        if len(boxs) > 0:
            frame = track(frame, tracker, encoder, boxs)
        if frame_check is None:
            frame_check = frame
        video_output.write(frame)
        ret, frame = cap.read()

if __name__ == "__main__":

    detection()