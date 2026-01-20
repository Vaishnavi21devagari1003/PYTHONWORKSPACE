import sqlite3

# Base Class (Inheritance)
class Person:
    def __init__(self, name, age):
        self._name = name   # Encapsulation
        self._age = age

    def display_info(self):
        return f"Name: {self._name}, Age: {self._age}"

# Derived Class (Inheritance + Polymorphism)
class Student(Person):
    def __init__(self, name, age, roll_number, marks):
        super().__init__(name, age)
        self.__roll_number = roll_number   # Encapsulation
        self.__marks = marks

    # Getter and Setter (Encapsulation)
    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def get_roll_number(self):
        return self.__roll_number

    # Polymorphism (Overriding)
    def display_info(self):
        return f"Student: {self._name}, Roll: {self.__roll_number}, Marks: {self.__marks}"

# Abstraction: Database Manager
class DatabaseManager:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                roll_number TEXT UNIQUE,
                marks INTEGER
            )
        """)
        self.conn.commit()

    def add_student(self, student: Student):
        try:
            self.cursor.execute("INSERT INTO students (name, age, roll_number, marks) VALUES (?, ?, ?, ?)",
                                (student._name, student._age, student.get_roll_number(), student.get_marks()))
            self.conn.commit()
            print("Student added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Roll number already exists. Student not added.")

    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def update_marks(self, roll_number, new_marks):
        self.cursor.execute("UPDATE students SET marks=? WHERE roll_number=?", (new_marks, roll_number))
        self.conn.commit()

    def delete_student(self, roll_number):
        self.cursor.execute("DELETE FROM students WHERE roll_number=?", (roll_number,))
        self.conn.commit()

    def search_student(self, keyword):
        # Search by roll number OR partial name
        self.cursor.execute("SELECT * FROM students WHERE roll_number=? OR name LIKE ?", (keyword, f"%{keyword}%"))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Menu-driven interface
def main():
    db = DatabaseManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            roll = input("Enter roll number: ")
            marks = int(input("Enter marks: "))
            student = Student(name, age, roll, marks)
            db.add_student(student)

        elif choice == "2":
            students = db.get_students()
            if students:
                for s in students:
                    print(s)
            else:
                print("No students found.")

        elif choice == "3":
            roll = input("Enter roll number: ")
            new_marks = int(input("Enter new marks: "))
            db.update_marks(roll, new_marks)
            print("Marks updated successfully!")

        elif choice == "4":
            roll = input("Enter roll number: ")
            db.delete_student(roll)
            print("Student deleted successfully!")

        elif choice == "5":
            keyword = input("Enter roll number or name to search: ")
            results = db.search_student(keyword)
            if results:
                for r in results:
                    print(r)
            else:
                print("No student found.")

        elif choice == "6":
            db.close()
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
