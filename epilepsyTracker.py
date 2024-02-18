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
async def open_stream(url, websocket):
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
    list_video_times = []
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
                start_time_display = round(flashing_lights_start_time - start_time, 1)
                end_time_display = round(flashing_lights_end_time - start_time, 1)
                
                curr = [start_time_display, start_time_display]
                print(curr)
                if len(list_video_times) <= 0:
                    list_video_times.append(curr)
                else:
                    relevant_tuple = list_video_times[-1]
                    a = relevant_tuple[1]
                    int(a)
                    if a+1.35 >= curr[1]:
                        curr[0] = relevant_tuple[0]
                        list_video_times.pop()
                    list_video_times.append(curr)
                #convert the list to a json string
                list_video = json.dumps(list_video_times)
                await websocket.send(list_video)

                # singular time
                if abs(start_time_display - end_time_display) <= 1:
                    video_time = f"{start_time_display}"
                    print(f"Flashing Light: {start_time_display}")
                # range of times
                else:
                    # video_time = (f"{start_time_display} - {end_time_display}")
                    video_time = f"{start_time_display} - {end_time_display}"
                    print(f"Flashing Light Duration: {flashing_lights_start_time - start_time} - {flashing_lights_end_time - start_time}")
                list_video_times.append("\n" + video_time)
                await websocket.send(list_video_times)

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
    
def close_stream(stream):
    cv2.destroyAllWindows()
    # close output window

    # safely close video stream.
    stream.stop()

    
# # This is a tester main function 
# if __name__ == "__main__":
#     # open_stream('https://youtu.be/dQw4w9WgXcQ')
#     # Scary one
#     # open_stream("https://www.youtube.com/watch?v=8iUEjjI4kik")
#     # Strobe with delay (white and black)
#     open_stream("https://www.youtube.com/watch?v=ZQfy2i4bpCA")
#     # Red and blue strobe 
#     #open_stream("https://www.youtube.com/watch?v=sCe58cZ2_tA")
    
    