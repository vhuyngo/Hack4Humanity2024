#pip install pafy
#sudo pip install --upgrade youtube_dl
import cv2, pafy
from flask_framework.py import flask_framework

# url = "https://www.youtube.com/watch______"
url = "https://www.youtube.com/watch?v=QdMiVGKvtMQ"

def rgb_check(url):
    frame = open_video(url)

    # Get the color of the top-left pixel (assuming the video is in BGR format)
    top_left_color = frame[0, 0]

    # Release the video capture object
    cap.release()

    return top_left_color
    

def open_video(url):
    video = pafy.new(url)
    best = video.getbest(preftype="webm")
    #documentation: https://pypi.org/project/pafy/

    capture = cv2.VideoCapture(best.url)
    check, frame = capture.read()
    print (check, frame)

    cv2.imshow('frame',frame)
    cv2.waitKey(10)

    capture.release()
    cv2.destroyAllWindows()
    return frame

def close_video(url):
    pass
