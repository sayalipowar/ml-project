import cv2
import pytesseract
import numpy as np
import os

# ✅ Define the correct image path
image_path = r"C:\Users\sajiy\technical presentation\mongodb_image.jpg"

# ✅ Check if the file exists before loading
if not os.path.exists(image_path):
    print(f"⚠️ Error: File '{image_path}' not found! Check the path.")
    exit()

# ✅ Load the image
image = cv2.imread(image_path)

# ✅ Verify if the image is loaded properly
if image is None:
    print("⚠️ Error: OpenCV couldn't read the image. Check file format and integrity.")
    exit()

# ✅ Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ✅ Apply Adaptive Thresholding for better contrast
processed = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

# ✅ Optional: Apply noise removal using a morphological operation
kernel = np.ones((1, 1), np.uint8)
processed = cv2.morphologyEx(processed, cv2.MORPH_CLOSE, kernel)

# ✅ Define OCR settings
custom_config = r'--oem 3 --psm 6'  # OCR mode

# ✅ Extract text using Tesseract OCR
text = pytesseract.image_to_string(processed, config=custom_config)

# ✅ Display extracted text
print("\n🔵 Improved Extracted Text:\n")
print(text)

# ✅ Save extracted text to a file
text_path = r"C:\Users\sajiy\technical presentation\improved_extracted_text.txt"
with open(text_path, "w", encoding="utf-8") as file:
    file.write(text)

print(f"\n✅ Extracted text saved at: {text_path}")
