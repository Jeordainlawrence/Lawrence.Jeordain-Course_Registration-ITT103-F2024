# Functions
# Representing a course, this class has an ID, name, and cost
class Course:
    def __init__(self, course_id, name, cost):
        self.course_id = course_id
        self.name = name
        self.cost = cost


# Represents a student and includes their ID, name, and email
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0

    # Enrolls students, checks for duplicates, and updates the course fee
    def enroll(self, course):
        if course in self.courses:
            raise ValueError(f"{self.name} is already enrolled in {course.name}")
        self.courses.append(course)
        self.balance += course.cost
        print(f"{self.name} is now enrolled in {course.name}")

    # Total fee for registered courses calculated
    def get_total_fee(self):
        return sum(course.cost for course in self.courses)


# This class manages enrollment for both students and courses
class RegistrationSystem:
    def __init__(self):
        self.courses = []  # List of courses
        self.students = {}  # Dictionary of student_id: Student objects

    # Add courses
    def add_course(self, course_id, name, cost):
        if any(course.course_id == course_id for course in self.courses):
            raise ValueError("Course ID already exists.")
        new_course = Course(course_id, name, cost)
        self.courses.append(new_course)
        print("Course has been added successfully.")

    # Register students in the system
    def register_student(self, student_id, name, email):
        if student_id in self.students:
            raise ValueError("Student ID is already registered.")
        new_student = Student(student_id, name, email)
        self.students[student_id] = new_student
        print("Student has been registered successfully.")

    # Enroll a student in a course
    def enroll_in_course(self, student_id, course_id):
        student = self.students.get(student_id)
        if not student:
            raise ValueError("Student ID not found.")

        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            raise ValueError("Course ID not found.")

        student.enroll(course)

    # Calculate payment
    def calculate_payment(self, student_id, payment_amount):
        student = self.students.get(student_id)
        if not student:
            raise ValueError("Student ID not found.")

        if payment_amount < 0.4 * student.balance:
            raise ValueError("A minimum payment of 40% is required.")
        student.balance -= payment_amount
        print(f"Payment of ${payment_amount:.2f} received. Remaining balance: ${student.balance:.2f}.")

    # Check student balance
    def check_student_balance(self, student_id):
        student = self.students.get(student_id)
        if not student:
            raise ValueError(f"No student found with ID {student_id}")

        print(f"Balance for {student.name}: ${student.balance:.2f}")

    # Show available courses
    def show_courses(self):
        if not self.courses:
            print("No courses available. Please add a course before utilizing this option.")
            return
        print("Available courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}, Cost: ${course.cost}")

    # Show registered students
    def show_registered_students(self):
        if not self.students:
            print("No students registered. Please register a student to utilize this option.")
            return
        print("Registered students:")
        for student in self.students.values():
            print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

    # Show students in a specific course
    def show_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print(f"Course ID {course_id} not found.")
            return

        print(f"Students enrolled in {course.name}:")
        enrolled_students = [student.name for student in self.students.values() if course in student.courses]
        if not enrolled_students:
            print("No students are currently enrolled in this course.")
        else:
            for name in enrolled_students:
                print(f"- {name}")


# Main Menu
def main():
    system = RegistrationSystem()
    while True:
        print("\nWelcome! Please select an option:")
        print("1. Register a student")
        print("2. Add a course")
        print("3. Enroll a student in a course")
        print("4. Calculate payment")
        print("5. Show registered students")
        print("6. Show courses")
        print("7. Check student balance")
        print("8. Show students in a course")
        print("9. Exit")

        try:
            option = int(input("Please select an option (1-9): "))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        try:
            if option == 1:
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                email = input("Enter student email: ")
                system.register_student(student_id, name, email)

            elif option == 2:
                course_id = input("Enter course ID: ")
                name = input("Enter course name: ")
                cost = float(input("Enter course cost: "))
                system.add_course(course_id, name, cost)

            elif option == 3:
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                system.enroll_in_course(student_id, course_id)

            elif option == 4:
                student_id = input("Enter student ID: ")
                payment = float(input("Enter payment amount: "))
                system.calculate_payment(student_id, payment)

            elif option == 5:
                system.show_registered_students()

            elif option == 6:
                system.show_courses()

            elif option == 7:
                student_id = input("Enter student ID: ")
                system.check_student_balance(student_id)

            elif option == 8:
                course_id = input("Enter course ID: ")
                system.show_students_in_course(course_id)

            elif option == 9:
                print("Exiting system. Goodbye!")
                break

            else:
                print("Invalid option. Please select a number between 1 and 9.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
