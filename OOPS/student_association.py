class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []   # association: teacher has students

    def add_student(self, student):
        self.students.append(student)

    def get_strength(self):
        return len(self.students)   # total number of students

    def find_marks_by_name(self, student_name):
        for s in self.students:
            if s.name.lower() == student_name.lower():  # case-insensitive match
                return s.marks
        return None   # if not found

    def remove_low_scorers(self, threshold=20):
        # Keep only students with marks >= threshold
        self.students = [s for s in self.students if s.marks >= threshold]

    def display_descending(self):
        # Sort by marks descending
        sorted_students = sorted(self.students, key=lambda s: s.marks, reverse=True)
        print("\nStudents in descending order of marks:\n")
        for s in sorted_students:
            s.show_details()
            print("----")

    def count_by_classification(self):
        counts = {"First Class": 0, "Second Class": 0, "Pass Class": 0, "Fail": 0}
        for s in self.students:
            classification = s.get_classification()
            counts[classification] += 1
        print("\nClassification counts:")
        for k, v in counts.items():
            print(f"{k}: {v}")


class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def get_classification(self):
        if self.marks >= 60:
            return "First Class"
        elif self.marks >= 50:
            return "Second Class"
        elif self.marks >= 35:
            return "Pass Class"
        else:
            return "Fail"

    def show_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Result: {self.get_classification()}")


# Example usage
teacher = Teacher("Dr. Smith")

# Add students
teacher.add_student(Student(101, "Alice", 72))
teacher.add_student(Student(102, "Bob", 55))
teacher.add_student(Student(103, "Charlie", 30))
teacher.add_student(Student(104, "David", 15))  # low scorer

# Remove students below 20 marks
teacher.remove_low_scorers()

# Display all students
print(f"{teacher.name} teaches the following students:\n")
for s in teacher.students:
    s.show_details()
    print("----")

# Show total strength
print(f"Total strength of class: {teacher.get_strength()}")

# Ask user for a name and show marks
name_to_search = input("\nEnter student name to get marks: ")
marks = teacher.find_marks_by_name(name_to_search)

if marks is not None:
    print(f"{name_to_search}'s marks: {marks}")
else:
    print(f"Student {name_to_search} not found.")

# Display descending order
teacher.display_descending()

# Count by classification
teacher.count_by_classification()
