from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["auction_database"]
collection = db["auction_properties"]

# Load CSV data into Pandas DataFrame
csv_path = "auction_data.csv"
df = pd.read_csv(csv_path)

# Convert DataFrame to dictionary format for MongoDB
data_dict = df.to_dict(orient="records")

# Insert data into MongoDB
collection.insert_many(data_dict)

print("Data inserted into MongoDB successfully!")
