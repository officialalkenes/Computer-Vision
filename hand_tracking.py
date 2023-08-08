import cv2

# Load an image from file
image_path = 'cat.jpg'  
image = cv2.imread(image_path, 1)

if image is not None:
    # Display the loaded image
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows
else:
    print("Image not loaded or invalid image path.")
