from typing import Protocol, runtime_checkable
from abc import ABC, abstractmethod
from typing import List


@runtime_checkable
class Harbinger(Protocol):
    @abstractmethod
    def chill(self) -> str: ...

@runtime_checkable
class Omnivore(Protocol):
    @abstractmethod
    def hunt(self) -> str: ...

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_extra(self):
        if isinstance(self, Omnivore): return self.hunt()
        if isinstance(self, Harbinger): return self.chill()
        return ""

    def __str__(self):
        return f"{self.__class__.__name__} name = {self.name}, age = {self.age}. {self.get_extra()}"

class Dog(Animal, Omnivore):
    def hunt(self) -> str: return "I can hunt for robbers"

class Cat(Animal, Omnivore):
    def hunt(self) -> str: return "I can hunt for mice"

class Hamster(Animal, Harbinger):
    def chill(self) -> str: return "I can chill for 8 hours"

class GuineaPig(Animal, Harbinger):
    def chill(self): return f"I can chill for 12 hours"


def print_pets(args: List[Animal]):
    sorted_pets = sorted(args, key=lambda x: isinstance(x, Omnivore))
    for animal in sorted_pets:
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
        "hamster": Hamster,
        "guinea": GuineaPig
    }
    while len(pets) < user_num:
        p_type = input().lower()
        if p_type in pet_classes:
            try:
                name = input()
                age = int(input())
                if age > 0:
                    cls = pet_classes.get(p_type)
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