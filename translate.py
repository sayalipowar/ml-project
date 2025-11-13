import json

def load_json(file_path):
    """Loads and returns data from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None

def display_properties(data):
    """Displays property details in a readable format."""
    if not data:
        print("No data available.")
        return
    
    for i, property in enumerate(data, start=1):
        print(f"Property {i}:")
        print(f"  Description: {property.get('Property Description', 'N/A')}")
        print(f"  Price: {property.get('Price', 'N/A')}")
        print(f"  Location: {property.get('Location', 'N/A')}")
        print(f"  Owner: {property.get('Owner', 'N/A')}")
        print("-" * 40)

def main():
    file_path = "C:/Users/sajiy/technical presentation/structured_data.json"
    data = load_json(file_path)
    display_properties(data)

if __name__ == "__main__":
    main()
