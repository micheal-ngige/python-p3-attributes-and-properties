#!/usr/bin/env python3


class Dog:

    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]
    def __init__(self, name="fido"):
        assert 1 <= len(name) <= 25 or name == {name},"name must be string between 1 and 25 characters."
        self.name= name

    @classmethod
    def approved_breed(cls, breed: str):
        assert breed in cls.APPROVED_BREEDS, "Breed must be in the list of approved breeds."
        return breed
       

        

my_dog= Dog("fido")
print(my_dog.name)
breed_check = "Pug"
result = Dog.approved_breed(breed_check)
print(result)