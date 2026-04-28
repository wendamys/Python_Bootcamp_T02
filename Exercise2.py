from abc import ABC


def print_pets(args):
    for item in args:
        print(item)


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
                        continue
                    user_input_wt_animal = input()
                    user_input_wt_animal = float(user_input_wt_animal)
                    if user_input_wt_animal <= 0:
                        print("Incorrect input. Mass <= 0")
                        user_num -= 1
                        continue
                    else:
                        if user_input_animal == "dog":
                            animal = self.Dog(user_input_name_animal, user_input_age_animal, user_input_wt_animal)
                        else:
                            animal = self.Cat(user_input_name_animal, user_input_age_animal, user_input_wt_animal)
                        items_animals.append(animal)
                except ValueError:
                    print("Could not parse a number. Please, try again")
                    user_num -= 1
            else:
                print("Incorrect input. Unsupported pet type")
                user_num -= 1

        return items_animals


    class Animal(ABC):
        def __init__(self, name, age, wt):
            self.__name = name
            self.__age = age
            self.__wt = wt


        def get_name(self):
            return self.__name


        def get_age(self):
            return self.__age

        def get_feed_info_kg(self):
            return self.__wt


    class Dog(Animal):
        def __init__(self, name, age, wt):
            super().__init__(name, age, wt)
            self.wt = wt

        def __str__(self):
            return f"Dog name = {self.get_name()}, age = {self.get_age()}, mass = {self.wt}, feed = {self.get_feed_info_kg()}"

        def get_feed_info_kg(self):
            return round(self.wt * 0.3, 2)

    class Cat(Animal):
        def __init__(self, name, age, wt):
            super().__init__(name, age, wt)
            self.wt = wt

        def __str__(self):
            return f"Cat name = {self.get_name()}, age = {self.get_age()}, mass = {self.wt}, feed = {self.get_feed_info_kg()}"

        def get_feed_info_kg(self):
            return round(self.wt * 0.1, 2)


obj2 = Exercise1()
array = obj2.input_user()
print_pets(array)