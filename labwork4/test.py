class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_age(self):
        return self.name + str(self.age)

    def name_bin_age(self):
        return self.name + " " + str(bin(self.age))


if __name__ == "__main__":
    Oleh = Student("Oleh", 23)
    print(Oleh.name_bin_age())
