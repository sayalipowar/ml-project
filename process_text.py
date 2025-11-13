import pandas as pd

# Load the extracted text file
with open("extracted_text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Define CSV columns
columns = [
    "S.No", "Name of Borrower & Bank Branch", "Date of Demand Notice & Amount", 
    "Description of Property", "Possession Status", "Reserve Price", 
    "EMD Amount", "Date & Time of Auction", "Incremental Bid Amount", "Authorised Officer"
]

# Initialize an empty list to store row data
data = []

# Parse text and store in structured format
for line in lines:
    parts = line.split("\t")  # Adjust splitting based on OCR format
    if len(parts) >= 10:  # Ensure valid row
        data.append(parts[:10])  # Keep only the required columns

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save as CSV
csv_path = "auction_data.csv"
df.to_csv(csv_path, index=False)

print(f"CSV file saved as '{csv_path}'.")
