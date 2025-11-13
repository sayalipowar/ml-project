
import cv2
import pytesseract

# Correct file path
image_path = r"C:\Users\sajiy\technical presentation\mongodb_image.jpg"

# Load the image
image = cv2.imread(image_path)

# Check if image was loaded properly
if image is None:
    print("Error: Could not read the image file. Check the file path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR
    text = pytesseract.image_to_string(gray, lang="eng")

    # Print extracted text
    print(text)
