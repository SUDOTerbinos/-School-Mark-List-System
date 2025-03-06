class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Marks      : {self.marks}")
        print(f"Total Marks: {self.total_marks()}")
        print(f"Average    : {self.average_marks():.2f}")
        print("----------------------------")


def main():
    students = []
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Student Name: ")
            roll_no = input("Enter Roll Number: ")
            subjects = int(input("Enter Number of Subjects: "))
            marks = []
            for i in range(subjects):
                mark = int(input(f"Enter marks for Subject {i+1}: "))
                marks.append(mark)

            student = Student(name, roll_no, marks)
            students.append(student)
            print("Student Added Successfully!\n")

        elif choice == '2':
            print("\nStudents List")
            print("==========================")
            for student in students:
                student.display()

        elif choice == '3':
            print("Exiting...")n            break

        else:
            print("Invalid Choice! Try Again.")


if __name__ == "__main__":
    main()