# import libraries
from pytube import YouTube 
from vidgear.gears import CamGear
import cv2

def open_stream(url):
    # rickroll
    # stream = CamGear(source='https://youtu.be/dQw4w9WgXcQ', stream_mode = True, logging=True).start() 
    # informational vid abt epilepsy for testing
    # stream = CamGear(source='https://www.youtube.com/watch?v=QdMiVGKvtMQ', stream_mode = True, logging=True).start() # YouTube Video URL as input
    stream = CamGear(source=url, stream_mode = True, logging=True).start() 
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
        
        delay = (int) (get_frame_rate(url))
        key = cv2.waitKey(delay) & 0xFF

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

def get_frame_rate(video_url):
    try:
        # Create a YouTube object
        youtube = YouTube(video_url)

        # Get the video stream with the highest resolution
        video_stream = youtube.streams.get_highest_resolution()
        print(video_stream.fps)

        return video_stream.fps

    except Exception as e:
        print("Error:", str(e))
        
# This is a tester main function 
if __name__ == "__main__":
    open_stream('https://youtu.be/dQw4w9WgXcQ')