import cv2
from vidgear.gears import CamGear

def detect_flashing_lights(frame):
    # Convert frame to grayscale for simplicity
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the standard deviation of pixel intensities
    std_dev = cv2.meanStdDev(gray)[1][0][0]

    # If standard deviation is above a certain threshold, consider it as flashing lights
    # return std_dev > 30
    return std_dev > 100

# Initialize video stream
stream = CamGear(source='https://www.youtube.com/watch?v=QdMiVGKvtMQ', stream_mode=True, logging=True).start()

# Infinite loop to read frames
while True:
    frame = stream.read()

    # Check if frame is None
    if frame is None:
        break

    # Do something with the frame here, like detecting flashing lights
    if detect_flashing_lights(frame):
        print("Flashing lights detected!")

    # Display the frame
    cv2.imshow("Output Frame", frame)

    # Check for 'q' key press to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Close all windows and stop the video stream
cv2.destroyAllWindows()
stream.stop()
