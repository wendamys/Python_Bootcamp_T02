from abc import ABC

class Exercise1:

    def input_user(self):
        while True:
            try:
                user_input = input()
                user_num = int(user_input)
                break
            except ValueError:
                print("Could not parse a number. Please, try again")
        items_animals = []
        while len(items_animals) < user_num:
            user_input_animal = input()
            if user_input_animal == "dog" or user_input_animal == "cat":
                try:
                    user_input_name_animal = input()
                    user_input_age_animal = input()
                    user_input_age_animal = int(user_input_age_animal)
                    if user_input_age_animal <= 0:
                        print("Incorrect input. Age <= 0")
                        user_num -= 1
                    else:
                        if user_input_name_animal == "dog":
                            animal = self.Dog(user_input_name_animal, user_input_age_animal)
                        else:
                            animal = self.Cat(user_input_name_animal, user_input_age_animal)
                        items_animals.append(animal)
                except ValueError:
                    print("Could not parse a number. Please, try again")
            else:
                print("Incorrect input. Unsupported pet type")
                user_num -= 1

        return items_animals

    def print_pets(self, args):
        for animal in args:
            print(animal)


    class Animal(ABC):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def get_name(self):
            return self.name

        def get_age(self):
            return self.age


    class Dog(Animal):
        def __init__(self, name, age):
            super().__init__(name, age)

        def __str__(self):
            return f"Dog name = {self.get_name()}, age = {self.get_age()}"

    class Cat(Animal):
        def __init__(self, name, age):
            super().__init__(name, age)


        def __str__(self):
            return f"Cat name = {self.get_name()}, age = {self.get_age()}"


obj1 = Exercise1()
items = obj1.input_user()
obj1.print_pets(items)