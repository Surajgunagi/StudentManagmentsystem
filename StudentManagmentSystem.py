# Student Management System using Dictionaries and Sets

students = {}   # Dictionary to store student data
courses = set() # Set to store all unique courses

# Function to add a new student
def add_student():
    student_id = input("Enter Student ID: ").strip()
    if student_id in students:
        print(" Student ID already exists!")
        return
    
    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    enrolled_courses = input("Enter courses (comma separated): ").split(",")
    enrolled_courses = [c.strip() for c in enrolled_courses]

    students[student_id] = {
        "name": name,
        "age": age,
        "courses": set(enrolled_courses)
    }
    courses.update(enrolled_courses)
    print(f" Student {name} added successfully!")

# Function to remove a student
def remove_student():
    student_id = input("Enter Student ID to remove: ").strip()
    if student_id in students:
        removed = students.pop(student_id)
        print(f" Removed student: {removed['name']}")
    else:
        print(" Student ID not found!")

# Function to update student info
def update_student():
    student_id = input("Enter Student ID to update: ").strip()
    if student_id in students:
        print("Enter new details (leave blank to keep current):")
        name = input("New Name: ").strip()
        age = input("New Age: ").strip()
        enrolled_courses = input("New Courses (comma separated): ").strip()

        if name:
            students[student_id]["name"] = name
        if age:
            students[student_id]["age"] = age
        if enrolled_courses:
            new_courses = [c.strip() for c in enrolled_courses.split(",")]
            students[student_id]["courses"] = set(new_courses)
            courses.update(new_courses)

        print(" Student updated successfully!")
    else:
        print(" Student ID not found!")

# Function to search student
def search_student():
    student_id = input("Enter Student ID to search: ").strip()
    if student_id in students:
        print(f" Found Student: {students[student_id]}")
    else:
        print(" Student not found!")

# Function to display all students
def display_students():
    print("\n Student List:")
    if not students:
        print("No students available.")
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Age: {info['age']} | Courses: {', '.join(info['courses'])}")

# Function to display all courses
def display_courses():
    print("\n All Courses Offered:")
    if not courses:
        print("No courses available.")
    for course in courses:
        print(f"- {course}")

# Function to show students in a course
def students_in_course():
    course_name = input("Enter course name: ").strip()
    print(f" Students in {course_name}:")
    found = False
    for sid, info in students.items():
        if course_name in info["courses"]:
            print(f"ID: {sid} | Name: {info['name']}")
            found = True
    if not found:
        print(" No students enrolled in this course.")

# Function to show statistics
def statistics():
    print(" Statistics:")
    print(f"Total Students: {len(students)}")
    print(f"Total Courses: {len(courses)}")

# ------------------- MAIN MENU -------------------
def main():
    while True:
        print(" \n Student Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Display All Courses")
        print("7. Show Students in a Course")
        print("8. Show Statistics")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            display_students()
        elif choice == "6":
            display_courses()
        elif choice == "7":
            students_in_course()
        elif choice == "8":
            statistics()
        elif choice == "9":
            print(" Exiting Student Management System. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":

    main()
