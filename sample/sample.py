class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def display(self):
        print("Name:", self.name)
        print("Mark:", self.mark)

s1 = Student("Arun", 90)
s1.display()