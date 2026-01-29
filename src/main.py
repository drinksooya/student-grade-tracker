import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "grades.json")

def load_data():
    """ Loads data """

    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print(f"Error: The file {DATA_FILE} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON. Check if the file format is valid.")

def save_data(data_to_save):
    """ Saves data in a .json file """

    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data_to_save, file, indent=4)

        print("✅ Grade added successfully!")
        print(f"Data successfully saved to {DATA_FILE}")

    except Exception as e:
        print(f"An error occurred while saving contacts: {e}")

def add_grade(grades_list):
    while True:
        quarter = input("Enter Quarter (e.g., Q1, Q2): ")
        subject = input("Enter Subject: ")

        if not subject.replace(" ", "").isalpha():
            print("Invalid Input: Please use letters for the subject name.")
            continue
        try:
            grade = float(input(f"Enter Grade for {subject}: "))

            # Storing as a Dictionary for better organization
            new_entry = {
                "quarter": quarter,
                "subject": subject,
                "grade": grade
            }

            grades_list.append(new_entry)
            save_data(grades_list)
            break
        except ValueError:
            print("Invalid input.")


def view_grades(grades_list):
    if not grades_list:
        print("\nNo grades added yet.")
        return

    # 1. Get unique quarters
    quarters = sorted(list(set(item['quarter'] for item in grades_list)))

    print("\n" + "=" * 45)
    print(f"{'ID':<4} | {'Subject':<15} | {'Grade':<5}")

    for q in quarters:
        print("-" * 45)
        print(f"--- QUARTER: {q} ---")
        print("-" * 45)

        # We'll use these to track the average for THIS quarter
        q_total = 0
        q_count = 0

        for index, item in enumerate(grades_list, start=1):
            if item['quarter'] == q:
                s = item.get("subject", "N/A")
                g = item.get("grade", 0.0)
                print(f"{index:<4} | {s:<15} | {g:<5}")

                # Update our math trackers
                q_total += g
                q_count += 1

        # 2. Print the average for the current quarter
        if q_count > 0:
            q_avg = q_total / q_count
            print(f"\n>> {q} Average: {q_avg:.2f}")

    print("=" * 45)
    print(f"Total Records: {len(grades_list)}\n")

def delete_grade(grade_list):
    """ Deletes Grades """

    view_grades(grade_list)

    if not grade_list:
        return

    try:
        choice = int(input("\nEnter the number of the grade to delete: "))
        index_to_delete = choice - 1

        if 0 <= index_to_delete < len(grade_list):
            removed_item = grade_list.pop(index_to_delete)
            print(f"Successfully deleted: {removed_item['subject']}")

            save_data(grade_list)
        else:
            print("Error: That number doesn't exist in the list.")

    except ValueError:
        print("Invalid input! Please enter a number.")

def menu(grade_list):
    """ Shows the whole menu """

    while True:
        print("\n")
        print(33 * "-")
        print("       📚 GRADE TRACKER")
        print(33 * "-")

        print("1. Add new grade")
        print("2. View all grades")
        print("3. Delete grade")
        print("4. Exit")
        print(33 * "-")

        user_input = input("\nEnter your choice: ").strip()

        if user_input == "1":
            add_grade(grade_list)
        elif user_input == "2":
            view_grades(grade_list)
        elif user_input == "3":
            delete_grade(grade_list)
        elif user_input == "4":
            print("Exiting app...")
            break
        else:
            print("Invalid choice, please pick 1-4.")

if __name__ == "__main__":
    all_student_grades = load_data() or []
    menu(all_student_grades)