# import libraries
from pytube import YouTube 
from vidgear.gears import CamGear
import cv2
import time

def detect_flashing_lights(prev_frame, frame, min_std_dev, max_std_dev):
    # Convert frame to grayscale for simplicity
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the frames
    difference = cv2.absdiff(prev_gray, gray)
    # print(difference) - matri

    # Calculate the standard deviation of pixel intensities
    std_dev = cv2.meanStdDev(difference)[1][0][0]

    if min_std_dev <= std_dev <= max_std_dev:
        return True, time.time()
    else:
        return False, None

# def open_stream(url, websocket):
def open_stream(url, websocket):
    # rickroll
    # stream = CamGear(source='https://youtu.be/dQw4w9WgXcQ', stream_mode = True, logging=True).start() 
    print("It is reaching right before the camgear")
    stream = CamGear(source=url, stream_mode = True, logging=True).start() 
    print("It is reaching right after the camgear")
    # print(type(stream))

    # get frame rate for delay
    frame_rate = (int) (get_frame_rate(url))
    # print(frame_rate)

    # get previous frame for comparison, start as none
    prev_frame = None

    # define range for standard dev of flashing lights
    minimum_standard_deviation = 8
    maximum_standard_deviation = 10

    # Flags and variables for flashing lights detection
    flashing_lights_detected = False
    flashing_lights_start_time = None
    flashing_lights_end_time = None

    start_time = time.time()
    # infinite loop
    while True:
        # read frames
        frame = stream.read()

        # check if frame is None and break
        if frame is None:
            break
        
        # do something with frame here
        #     if detect_flashing_lights(prev_frame, frame):
        #         print("Flashing lights detected!")
        if prev_frame is not None:
            # if detect_flashing_lights(prev_frame, frame, minimum_standard_deviation, maximum_standard_deviation):
            #     print("Flashing lights detected!")
            detected, timestamp = detect_flashing_lights(prev_frame, frame, minimum_standard_deviation, maximum_standard_deviation)
            if detected:
                if not flashing_lights_detected:
                    flashing_lights_detected = True
                    flashing_lights_start_time = time.time()
            elif flashing_lights_detected:
                flashing_lights_detected = False
                flashing_lights_end_time = time.time()
                # We can use these variables
                # start_time_display = flashing_lights_start_time - start_time
                # end_time_display = flashing_lights_end_time - start_time
                video_time = f"Flashing lights event duration: {flashing_lights_start_time - start_time} - {flashing_lights_end_time - start_time}"
                websocket.send(video_time)
                print(f"Flashing lights event duration: {flashing_lights_start_time - start_time} - {flashing_lights_end_time - start_time}")

        # update the previous frame
        # TODO: Might have to change prev_frame
        prev_frame = frame.copy()
        
        cv2.imshow("Output Frame", frame)
        # Show output window
        
        # key = cv2.waitKey(delay) & 0xFF
        key = cv2.waitKey(frame_rate) & 0xFF

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
        # print(f"FPS: {video_stream.fps}")
        # print(f"delay (ms): {(1/video_stream.fps) * 1000}")

        return video_stream.fps

    except Exception as e:
        print("Error:", str(e))
        
# # This is a tester main function 
# if __name__ == "__main__":
#     # open_stream('https://youtu.be/dQw4w9WgXcQ')
#     # Scary one
#     # open_stream("https://www.youtube.com/watch?v=8iUEjjI4kik")
#     # Strobe with delay (white and black)
#     open_stream("https://www.youtube.com/watch?v=ZQfy2i4bpCA")
#     # Red and blue strobe 
#     #open_stream("https://www.youtube.com/watch?v=sCe58cZ2_tA")
    
    