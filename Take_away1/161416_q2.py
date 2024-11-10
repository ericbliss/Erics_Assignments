class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"Grades for {self.name} (ID: {self.student_id}):")
        for assignment, grade in self.assignments.items():
            print(f"  {assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Assigned grade {grade} for {assignment_name} to {student.name}")
                return
        print(f"No student found with ID: {student_id}")

    def display_all_students_grades(self):
        print(f"Grades for course: {self.course_name}")
        for student in self.students:
            student.display_grades()

    def interactive_mode(self):
        while True:
            action = input("Choose an action: [1] Add student, [2] Assign grade, [3] Display grades, [4] Exit: ")
            if action == '1':
                name = input("Enter student's name: ")
                student_id = input("Enter student's ID: ")
                student = Student(name, student_id)
                self.add_student(student)
                print(f"Added student {name} with ID {student_id}.")
            elif action == '2':
                student_id = input("Enter student's ID: ")
                assignment_name = input("Enter assignment name: ")
                grade = input("Enter grade: ")
                self.assign_grade(student_id, assignment_name, grade)
            elif action == '3':
                self.display_all_students_grades()
            elif action == '4':
                print("Exiting interactive mode.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    instructor = Instructor(name="Samuel Githogori ", course_name="Intro to Programming")
    instructor.interactive_mode()
