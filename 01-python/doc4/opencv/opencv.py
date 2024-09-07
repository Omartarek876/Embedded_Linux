import cv2

def main():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)
    
    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return
    
    # Set the window name for the live video stream
    window_name = "Camera Preview"
    cv2.namedWindow(window_name)
    i = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Check if the frame was captured successfully
        if not ret:
            print("Error: Unable to capture frame.")
            break
        
        # Display the frame in a window
        cv2.imshow(window_name, frame)
        
        # Check for the 'c' key press
        key = cv2.waitKey(1)
        if key == ord('c'):  # Press 'c' key to take a picture
            # Save the captured frame as an image
            cv2.imwrite(f"images/captured_image{i}.jpg", frame)
            print("Image captured successfully!")
            i = i + 1
        # Break the loop when the 'q' key is pressed
        if key == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
