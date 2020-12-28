class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Hi, my name is " + self.name, ", I am " + str(self.age), "y.o.")

    def action(self):
        print("I am...")


class Students(People):

    def __init__(self, name, age, course, stress_level):
        super().__init__(name, age)
        self.course = course
        self.stress_level = stress_level

    def show_info(self):
        super().show_info()
        print("I am on " + str(self.course), "course")
        print("and my level of stress is " + str(self.stress_level))

    def action(self):
        super().action()
        print("studying")


class Pupils(People):

    def __init__(self, name, age, grade, fav_subject):
        super().__init__(name, age)
        self.grade = grade
        self.fav_subject = fav_subject

    def show_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Grade: " + str(self.grade))
        print("Favorite subject: " + self.fav_subject)

    def action(self):
        print("I go to school")


class Workers(People):

    def __init__(self, name, age, salary, experience):
        super().__init__(name, age)
        self.salary = salary
        self.experience = experience

    def show_info(self):
        super().show_info()
        print("I earn " + str(self.salary), "rub per hour")
        print("and this is my " + str(self.experience), "year on this factory")

    def action(self):
        print("I am working hard for misery salary")


class Qualification(Workers):

    def __init__(self, name, age, salary, experience, category=1):
        super().__init__(name, age, salary, experience,)
        self.category = category

    def show_info(self):
        super().show_info()
        print("my category: " + str(self.category))

    def action(self):
        super().action()
        print("help me pls!")
