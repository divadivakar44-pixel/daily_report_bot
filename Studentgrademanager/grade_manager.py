# grade_manager.py

students = []


def get_grade(mark):
    """Returns the letter grade based on the numeric mark."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    """Prompts for student name and valid mark (0-100), then stores them."""
    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty. Please enter a valid name.")
        name = input("Enter student name: ").strip()

    while True:
        try:
            mark = float(input(f"Enter mark for {name} (0-100): "))
            if 0 <= mark <= 100:
                break
            else:
                print("Error: Mark must be between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

    students.append({"name": name, "mark": mark})
    print(f"Successfully added {name} with a mark of {mark}.\n")


def show_results():
    """Prints the formatted results table, average, highest, and lowest marks."""
    if not students:
        print("\nNo student records available to display.\n")
        return

    print("\n" + "=" * 30)
    print(f"{'Name':<15} {'Mark':<8} {'Grade':<5}")
    print("-" * 30)

    total_marks = 0
    highest = students[0]["mark"]
    lowest = students[0]["mark"]

    for s in students:
        name = s["name"]
        mark = s["mark"]
        grade = get_grade(mark)

        # Format mark to display neatly as integer or 1-decimal float
        mark_str = f"{mark:.1f}".rstrip("0").rstrip(".")

        print(f"{name:<15} {mark_str:<8} {grade:<5}")

        total_marks += mark
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark

    avg = total_marks / len(students)

    print("-" * 30)
    print(f"Average: {avg:.1f}")
    print(
        f"Highest: {highest:.1f}".rstrip("0").rstrip(".")
        + f"  Lowest: {lowest:.1f}".rstrip("0").rstrip(".")
    )
    print("=" * 30 + "\n")


def main():
    """Main menu loop."""
    while True:
        print("--- Student Grade Manager ---")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
