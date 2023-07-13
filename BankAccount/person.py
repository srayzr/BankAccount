class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        if self.gender == "Male":
            return "{} {} - {}".format(self.name, self.surname, self.age)
        else:
            return "{} {}".format(self.name, self.surname)

    def add_age(self, n=1):
        self.age += n
