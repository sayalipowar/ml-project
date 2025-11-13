from PIL import Image
import pytesseract
import pandas as pd
from googletrans import Translator

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = r'C:\Users\sajiy\technical presentation\mongodb_image.jpg'
image = Image.open(image_path)

# Convert image to grayscale (optional preprocessing step)
image = image.convert('L')

# Perform OCR on the image to get detailed data
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

# Extract text and their positions
rows = []
for i in range(len(data['level'])):
    row = {
        'left': data['left'][i],
        'top': data['top'][i],
        'width': data['width'][i],
        'height': data['height'][i],
        'text': data['text'][i]
    }
    rows.append(row)

# Convert to DataFrame
df = pd.DataFrame(rows)

# Filter out empty text entries
df = df[df['text'].str.strip() != '']

# Save DataFrame to CSV
csv_file_path = r'C:\Users\sajiy\technical presentation\extracted_table.csv'
df.to_csv(csv_file_path, index=False)

# Extract text for translation
extracted_text = " ".join(df['text'].tolist())

# Save extracted text to a file
extracted_text_file_path = r'C:\Users\sajiy\technical presentation\extracted_text.txt'
with open(extracted_text_file_path, 'w', encoding='utf-8') as file:
    file.write(extracted_text)

# Translate the extracted text
translator = Translator()
translated_text = translator.translate(extracted_text, dest='en').text

# Save translated text to a file
translated_text_file_path = r'C:\Users\sajiy\technical presentation\translated_text.txt'
with open(translated_text_file_path, 'w', encoding='utf-8') as file:
    file.write(translated_text)

print("\n✅ Table extracted and saved successfully at:", csv_file_path)
print("✅ Extracted text saved successfully at:", extracted_text_file_path)
print("✅ Translated text saved successfully at:", translated_text_file_path)