import json
import os
import sys

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


def delete_grade(grade_list):
    # 1. Show the user what they are looking at
    view_grades(grade_list)

    if not grade_list:
        return

    try:
        choice = int(input("\nEnter the number of the grade to delete: "))
        index_to_delete = choice - 1

        if 0 <= index_to_delete < len(grade_list):
            removed_item = grade_list.pop(index_to_delete)
            print(f"Successfully deleted: {removed_item[0]}")

            save_data(grade_list)
        else:
            print("Error: That number doesn't exist in the list.")

    except ValueError:
        print("Invalid input! Please enter a number.")

def menu(grade_list):
    print(33 * "-")
    print("GRADE TRACKER")
    print(33 * "-")

    print("1. Add new grade")
    print("2. View all grades")
    print("3. Delete grade")
    print("4. Exit")
    print(33 * "-")

    while True:
        user_input = int(input("\nEnter your choice: "))

        if user_input == 1:
            add_grade(grade_list)
        elif user_input == 2:
            view_grades(grade_list)
        elif user_input == 3:
            delete_grade(grade_list)
        elif user_input == 4:
            sys.exit()
        else:
            print("Invalid choice")



if __name__ == "__main__":
    all_student_grades = load_data() or []
    menu(all_student_grades)