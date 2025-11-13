import cv2
import pytesseract
import re
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download("stopwords")

# ✅ Load the image
image_path = r"C:\Users\sajiy\technical presentation\mongodb_image.jpg"
image = cv2.imread(image_path)

if image is None:
    print("⚠️ Error: Could not read the image file. Check the file path.")
    exit()

# ✅ Preprocessing the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
gray = cv2.GaussianBlur(gray, (3, 3), 0)  # Apply noise reduction
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)  # Thresholding

# ✅ Perform OCR with better settings
custom_config = r'--oem 3 --psm 6'  
text = pytesseract.image_to_string(gray, config=custom_config, lang="eng")

# ✅ Save raw OCR output
ocr_text_file = r"C:\Users\sajiy\technical presentation\extracted_text.txt"
with open(ocr_text_file, "w", encoding="utf-8") as file:
    file.write(text)

print("\n✅ OCR extraction complete!")

# ✅ Clean the extracted text
text = re.sub(r'[^A-Za-z0-9\s.,:;/-]', ' ', text)  # Remove special characters
text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
lines = text.split(". ")  # Split into sentences

# ✅ Apply spell check
corrected_lines = [str(TextBlob(line).correct()) for line in lines]

# ✅ Save cleaned text
cleaned_file_path = r"C:\Users\sajiy\technical presentation\cleaned_text.txt"
with open(cleaned_file_path, "w", encoding="utf-8") as file:
    file.write("\n".join(corrected_lines))

print("\n✅ Cleaned and corrected text saved successfully!")

# ✅ Extract keywords
def extract_keywords(text, num_keywords=10):
    words = text.lower().split()
    words = [word for word in words if word not in stopwords.words("english")]
    word_counts = Counter(words)
    return [word for word, _ in word_counts.most_common(num_keywords)]

keywords = extract_keywords(" ".join(corrected_lines))

print("\n🔍 Top Keywords:", keywords)

# ✅ Save keywords
keywords_file = r"C:\Users\sajiy\technical presentation\keywords.txt"
with open(keywords_file, "w", encoding="utf-8") as file:
    file.write(", ".join(keywords))

print("\n✅ Keywords extracted and saved successfully!")
