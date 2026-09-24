class Student:
    def __init__(self, name = str, age = int, avg_score = int):
        self.name = name
        self.score = avg_score
        self.age = age

    def change_avg_score(self, new_avg_score = int):
        self.score = new_avg_score
    def __repr__(self):
        return f'Student {self.name}, {self.score}, {self.age}'
student = Student('Vova', 20, 90)
student.change_avg_score(100)
print(student)