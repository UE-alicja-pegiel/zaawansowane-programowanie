

class Student:
    def __init__(self, name: str, mark: float):
        self.name = name
        self.mark = mark

    def __str__(self):
        if self.is_passed():
            return f'Student {self.name} passed with the mark of {self.mark}.'
        return f'Student {self.name} did not pass with the mark of {self.mark}.'

    def is_passed(self) -> bool:
        if self.mark >= 50:
            return True
        return False


student1 = Student("Anna Nowak", 50)
student2 = Student("Jan Kowalski", 27)
print(student1)
print(student2)
