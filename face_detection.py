# Import the OpenCV library
import cv2

# Load the pre-trained face and eye detection Haar cascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


def detect(gray, frame):
    """
    Function to detect faces and eyes in an image.
    Takes a grayscale image (gray) and the original image (frame) as input.
    Returns the frame with rectangles drawn around detected faces and eyes.
    """
    
    # Detect faces in the grayscale image using the face cascade.
    # The detectMultiScale method detects objects of different sizes and
    # returns a list of rectangles, where each rectangle corresponds to a face.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Loop through all detected faces.
    for (x, y, w, h) in faces:
        # Draw a blue rectangle around each detected face in the original frame.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Define regions of interest (ROI) for both grayscale and color images.
        # These ROIs correspond to the area of the detected face.
        roi_gray = gray[y: y + h, x: x + w]
        roi_color = frame[y: y + h, x: x + w]
        
        # Detect eyes within the face's ROI using the eye cascade.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        
        # Loop through all detected eyes within the face.
        for (ex, ey, ew, eh) in eyes:
            # Draw a green rectangle around each detected eye in the color frame.
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 2), 2)
    
    # Return the frame with the drawn rectangles.
    return frame


# Start capturing video from the webcam (camera index 0)
video_capture = cv2.VideoCapture(0)

# Continuously capture frames from the webcam
while True:
    # Read the last frame captured by the webcam
    _, frame = video_capture.read()
    
    # Convert the frame to grayscale as the cascades require grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Call the detect function to detect faces and eyes, and draw rectangles around them
    canvas = detect(gray, frame)
    
    # Display the frame (with rectangles) in a window called "Video"
    cv2.imshow("Video", canvas)
    
    # Break the loop and exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and stop capturing video
video_capture.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
