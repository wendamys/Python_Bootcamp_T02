from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from typing import List

T = TypeVar('T')

class Base_Iterator(ABC, Generic[T]):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def hasNext(self):
        pass

    def reset(self):
        pass

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__} name = {self.name}, age = {self.age}"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Animal_Iterator(Base_Iterator[Animal]):
    def __init__(self, list_animal):
        self.list_animal = list(list_animal)
        self.current_index_list = 0

    def next(self) -> Animal:
        result = self.list_animal[self.current_index_list]
        self.current_index_list += 1
        return result

    def hasNext(self) -> bool:
        return self.current_index_list < len(self.list_animal)

    def reset(self):
        self.current_index_list = 0

def parse_int():
    while True:
        try:
            user_input = int(input())
            break
        except ValueError:
            print("Could not parse a number. Please, try again")
    return user_input


def input_user() -> List[Animal]:
    user_num = parse_int()
    pets = []
    pet_classes = {
        "dog": Dog,
        "cat": Cat,
    }
    while len(pets) < user_num:
        p_type = input().lower()
        if p_type in pet_classes:
            name = input()
            age = parse_int()
            if age > 0:
                cls = pet_classes.get(p_type)
                pets.append(cls(name, age))
            else:
                print("Incorrect input. Age <= 0")
                user_num -= 1
        else:
            print("Incorrect input. Unsupported pet type")
            user_num -= 1
    return pets

if __name__ == "__main__":
    pet_list = input_user()
    example  = Animal_Iterator(pet_list)
    while example.hasNext():
        print(example.next())
