class GroupLimitError(Exception):

    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"
        )


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record book: {self.record_book}"


class Group:
    MAX_STUDENTS = 10  # Ліміт студентів у групі

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupLimitError(
                f"Не можна додати більше {self.MAX_STUDENTS} студентів до групи {self.number}"
            )
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"


gr = Group("PD1")


for i in range(1, 11):
    gr.add_student(Student("Male", 20 + i, f"Name{i}", f"Surname{i}", f"AN{i}"))

print(gr)
try:
    gr.add_student(Student("Female", 22, "Extra", "Student", "AN999"))
except GroupLimitError as e:
    print(e)