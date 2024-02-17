# import libraries
from vidgear.gears import CamGear
import cv2

def open_stream(url):
    # rickroll
    # stream = CamGear(source='https://youtu.be/dQw4w9WgXcQ', stream_mode = True, logging=True).start() 
    # informational vid abt epilepsy for testing
    stream = CamGear(source='https://www.youtube.com/watch?v=QdMiVGKvtMQ', stream_mode = True, logging=True).start() # YouTube Video URL as input
    # stream = CamGear(source=url, stream_mode = True, logging=True).start() 
    print(type(stream))

    # infinite loop
    while True:
        frame = stream.read()
        # read frames

        # check if frame is None
        if frame is None:
            #if True break the infinite loop
            break
        
        # do something with frame here
        
        cv2.imshow("Output Frame", frame)
        # Show output window

        key = cv2.waitKey(1) & 0xFF

        # check for 'q' key-press
        if key == ord("q"):
            #if 'q' key-pressed break out
            close_stream(stream)

    return stream

def close_stream(stream):
    cv2.destroyAllWindows()
    # close output window

    # safely close video stream.
    stream.stop()






# #pip install pafy
# #sudo pip install --upgrade youtube_dl
# import cv2, pafy
# from flask_framework.py import flask_framework

# # url = "https://www.youtube.com/watch______"
# url = "https://www.youtube.com/watch?v=QdMiVGKvtMQ"

# def rgb_check(url):
#     frame = open_video(url)

#     # Get the color of the top-left pixel (assuming the video is in BGR format)
#     top_left_color = frame[0, 0]

#     # Release the video capture object
#     cap.release()

#     return top_left_color
    

# def open_video(url):
#     video = pafy.new(url)
#     best = video.getbest(preftype="webm")
#     #documentation: https://pypi.org/project/pafy/

#     capture = cv2.VideoCapture(best.url)
#     check, frame = capture.read()
#     print (check, frame)

#     cv2.imshow('frame',frame)
#     cv2.waitKey(10)

#     capture.release()
#     cv2.destroyAllWindows()
#     return frame

# def close_video(url):
    