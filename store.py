import pandas as pd
import json

# ✅ Read the cleaned text file
file_path = r"C:\Users\sajiy\technical presentation\cleaned_text.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # ✅ Read cleaned text line by line
except FileNotFoundError:
    print(f"⚠️ Error: Cleaned text file '{file_path}' not found! Run table.py first.")
    exit()

# ✅ Convert cleaned text into a DataFrame
df = pd.DataFrame({"Text": [line.strip() for line in lines]})

# ✅ Convert DataFrame to JSON
data_json = df.to_dict(orient="records")

# ✅ Save JSON file
json_file_path = r"C:\Users\sajiy\technical presentation\structured_data.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(data_json, json_file, indent=4, ensure_ascii=False)

print("\n✅ JSON file saved successfully at:", json_file_path)
