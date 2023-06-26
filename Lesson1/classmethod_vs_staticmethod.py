class Student:
    """ Class representing student in NCT-CSA09 """

    class_name = "NCT-CSA09"

    def __init__(self, name):
        self.name = name
    
    @classmethod
    def get_info(cls):
        return cls.class_name # This fine
        # return cls.name # This one should not work

    @classmethod
    def from_string(cls, s):
        """ A factory method to return a Student instance from a string """

        lst = s.split(', ')
        first_name, last_name, middle_name = lst
        fullname = last_name + " " + middle_name + " " + first_name
        return Student(fullname)

    @staticmethod
    def announce():
        print("This is a student from NCT-CSA09")

std_1 = Student("Viet")
print(Student.get_info())


# get student info from a string
s = "Viet, Ngo, Quang"
std_2 = Student.from_string(s)
print(std_2.name)

Student.announce()
