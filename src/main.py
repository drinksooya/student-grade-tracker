import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "..", "grades.json")

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print(f"Error: The file {DATA_FILE} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON. Check if the file format is valid.")

def save_data(data_to_save):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data_to_save, file, indent=4)

        print(f"Data successfully saved to {DATA_FILE}")

    except Exception as e:
        print(f"An error occurred while saving contacts: {e}")

def add_grade(grades):
    user_input = input("Enter your grade: ")

if __name__ == "__main__":
    # Test saving
    test_data = [{"id": 1, "text": "Test task"}]
    save_data(test_data)

    # Test loading
    loaded = load_data()
    print(loaded)  # Should print your test data