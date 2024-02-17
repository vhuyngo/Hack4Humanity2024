# import libraries
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

        key = cv2.waitKey(40) & 0xFF

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

# This is a tester main function 
if __name__ == "__main__":
    open_stream('https://youtu.be/dQw4w9WgXcQ')