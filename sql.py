class Subject:
    def __init__(self, subject, units, mark):
        self.subject = subject
        self.units = units
        self.mark = mark

    def __str__(self):
        return f"They got a mark of {self.mark} in {self.subject}"

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []
    
    def add_subject(self, subject, units, mark):
        new_subject = Subject(subject, units, mark)
        self.subjects.append(new_subject)
    
    def __str__(self):
        subject_list = [str(subject) for subject in self.subjects]
        return f"{self.name} does the following subjects: {', '.join(subject_list)}"

# Testing the classes
student = Student('tommy')

counter = 0 
while counter < 10:
    subject = input("What's the subject name? ")
    Set units = None
    while units not in [1,2]:
        try:
            units = int(input("How many units? "))
            break
        except ValueError:
            units = int(input("How many units? "))
    
    mark = None
    while mark < 0 or mark > 100:
        try:
            mark = int(input("What did you score? "))
            break
        except:
            mark = int(input("What did you score? "))
    counter += units
    student.add_subject (subject, units, mark)

for subject in student.subjects:
    print (subject.mark)
