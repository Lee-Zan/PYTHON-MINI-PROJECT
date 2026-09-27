class Student:

    college_name = "NSC College"
    def __init__(self, id, name, address, age, grade, subjects):
        self.id = id
        self.name = name
        self.address = address
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def display_info(self):
        print("---",Student.college_name,"---\n")
        print("Roll No.:",self.id)
        print("Name:",self.name)
        print("Address:",self.address)
        print("Age:",self.age)
        print("Grade:",self.grade)
        print("Subjects:",', '.join(self.subjects))
        print("------------------------------------------------------\n")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(student.name,"added successfully.\n")

    def remove_student(self, id):
        for i in self.students:
            if i.id == id:
                self.students.remove(i)
                print(i.name,"removed successfully.\n")
                return
        print("Student not found in record.\n")

    def list_student(self):
        if not self.students:
            print("No students available.\n")
        else:
            for i in self.students:
                i.display_info()


S1 = Student(101, "Lizan Niraula", "Bhaktapur", 22, 12, ["C", "Java", "Math", "Python", "Chemistry", "Biology"])
S2 = Student(102, "Ram Bahadur", "Kathmandu", 21, 12, ["History", "Mobile Programming", "Math", "HTML", "CSS", "JavaScript"])
S3 = Student(103, "Gita Kumari", "Lalitpur", 22, 12, ["C++", "Nepali", "English", "C#", "Economics", "Computer Science"])

manager = StudentManager()
manager.add_student(S1)
manager.add_student(S2)
manager.add_student(S3)

manager.list_student()

manager.remove_student(101)
manager.list_student()