class Student:
    def __init__(self, name = str, age = int, avg_score = int):
        self.name = name
        self.score = avg_score
        self.age = age

    def change_avg_score(self, new_avg_score = int):
        self.score = new_avg_score

student = Student('Vova', 20, 90)
print()
student.change_avg_score(100)
print(student.score)