from abc import ABC
from typing import List

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__} name = {self.name}, age = {self.age}"

class Dog(Animal): pass

class Cat(Animal): pass


def print_pets(args: List[Animal]):
    for animal in args:
        print(animal)

def input_user() -> List[Animal]:
    while True:
        try:
            user_num = int(input())
            break
        except ValueError:
            print("Could not parse a number. Please, try again")
    pets = []
    pet_classes = {
        "dog": Dog,
        "cat": Cat,
    }
    while len(pets) < user_num:
        p_type = input().lower()
        if p_type in pet_classes:
            try:
                name = input()
                age = int(input())
                if age > 0:
                    cls = pet_classes.get(p_type)
                    if age > 10: age += 1
                    pets.append(cls(name, age))
                else:
                    print("Incorrect input. Age <= 0")
                    user_num -= 1
            except ValueError:
                print("Could not parse a number. Please, try again")
        else:
            print("Incorrect input. Unsupported pet type")
            user_num -= 1
    return pets


if __name__ == "__main__":
    items = input_user()
    print_pets(items)