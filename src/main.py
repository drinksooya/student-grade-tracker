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


def add_grade(grades_list):
    """ Adds new grades """

    subject = input("Enter the subject name: ")
    user_input = input(f"Enter the grade for {subject}: ")

    try:
        grade = float(user_input)
        if 0 <= grade <= 100:
            grades_list.append((subject, grade))
            save_data(grades_list)
            print(f"Added {subject}: {grade}")
        else:
            print("Error: Grade must be 0-100.")
    except ValueError:
        print("Invalid input! Please enter a number.")


def view_grades(grades_list):
    """ Displays all grades """

    if not grades_list:
        print("No grades added yet.")
        return

    print("\n--- Student Grade Report ---")
    # Now this works because each item is a pair!
    for index, (subject, grade) in enumerate(grades_list, start=1):
        print(f"{index}. {subject}: {grade}%")


if __name__ == "__main__":
    all_student_grades = load_data() or []

    add_grade(all_student_grades)

    view_grades(all_student_grades)