import threading
import time
from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__class__.__name__} name = {self.name}, age = {self.age}"

    @abstractmethod
    def goToWalk(self):
        return 1

class Dog(Animal):
    def goToWalk(self):
        time_walking =  0.5 * self.age
        time.sleep(time_walking)
        return time_walking

class Cat(Animal):
    def goToWalk(self):
        time_walking = 0.25 * self.age
        time.sleep(time_walking)
        return time_walking

def parse_int():
    while True:
        try:
            user_input = int(input())
            break
        except ValueError:
            print("Could not parse a number. Please, try again")
    return user_input

def walk_pet(pet: Animal, start_program: float) -> None:
    walk_start = time.time()
    start_time = walk_start - start_program
    pet.goToWalk()
    walk_end = time.time()
    end_time = walk_end - start_program
    print(f"{pet.__class__.__name__} name = {pet.name}, age = {pet.age}, start time = {start_time:.2f}, end time = {end_time:.2f}")


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
    start_program = time.time()
    items = input_user()
    threads = []
    for item in items:
        t = threading.Thread(target=walk_pet, args=(item, start_program))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

