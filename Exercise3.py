from typing import Protocol, runtime_checkable
from abc import ABC, abstractmethod

@runtime_checkable
class Harbinger(Protocol):
    @abstractmethod
    def chill(self) -> str: ...

@runtime_checkable
class Omnivore(Protocol):
    @abstractmethod
    def hunt(self) -> str: ...


def print_pets(args):
    sorted_pets = sorted(args, key=lambda x: isinstance(x, Omnivore))
    for animal in sorted_pets:
        print(animal)

class Exercise3:

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
            if (user_input_animal == "dog" or user_input_animal == "cat"
                    or user_input_animal == "hamster" or user_input_animal == "guinea"):
                try:
                    user_input_name_animal = input()
                    user_input_age_animal = input()
                    user_input_age_animal = int(user_input_age_animal)
                    if user_input_age_animal <= 0:
                        print("Incorrect input. Age <= 0")
                        user_num -= 1
                    else:
                        if user_input_animal == "dog":
                            animal = self.Dog(user_input_name_animal, user_input_age_animal)
                        elif user_input_animal == "cat":
                            animal = self.Cat(user_input_name_animal, user_input_age_animal)
                        elif user_input_animal == "hamster":
                            animal = self.Hamster(user_input_name_animal, user_input_age_animal)
                        else:
                            animal = self.GuineaPig(user_input_name_animal, user_input_age_animal)
                        items_animals.append(animal)
                except ValueError:
                    print("Could not parse a number. Please, try again")
            else:
                print("Incorrect input. Unsupported pet type")
                user_num -= 1

        return items_animals


    class AnimalABC(ABC):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def get_name(self): return self.name
        def get_age(self): return self.age


    class Dog(AnimalABC, Omnivore):
        def __init__(self, name, age):
            super().__init__(name, age)
        def __str__(self): return f"Dog name = {self.get_name()}, age = {self.get_age()}. {self.hunt()}"
        def hunt(self) -> str: return "I can hunt for robbers"

    class Cat(AnimalABC, Omnivore):
        def __init__(self, name, age):
            super().__init__(name, age)
        def __str__(self): return f"Cat name = {self.get_name()}, age = {self.get_age()}. {self.hunt()}"
        def hunt(self) -> str: return "I can hunt for mice"

    class Hamster(AnimalABC, Harbinger):
        def __init__(self, name, age):
            super().__init__(name, age)
        def __str__(self): return f"Hamster name = {self.get_name()}, age = {self.get_age()}. {self.chill()}"
        def chill(self) -> str: return "I can chill for 8 hours"

    class GuineaPig(AnimalABC, Harbinger):
        def __init__(self, name, age):
            super().__init__(name, age)
        def chill(self) -> str: return "I can chill for 12 hours"
        def __str__(self): return f"GuineaPig name = {self.get_name()}, age = {self.get_age()}. {self.chill()}"


obj3 = Exercise3()
items = obj3.input_user()
print_pets(items)