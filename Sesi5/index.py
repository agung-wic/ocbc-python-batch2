class Dog:
    # Class attribute
    __species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.breed = breed

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old with species {self.__species}"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

buddy = Dog("BUddy", 9)
miles = Dog("Miles", 4)

print(buddy.name)
print(buddy.age)
print(buddy.__species)
print(miles.name)
print(miles.age)
# print(miles.species)

# buddy.species="bulldog"
buddy.name="regy"

# print(buddy.species)
print(buddy.name)
print(buddy.description())
# print(miles.species)

print(miles.description())
# print(miles.speak("Woof woof"))

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))


# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return f"{self.name} says {sound}"


# class Dachshund(Dog):
#     pass


# class Bulldog(Dog):
#     pass


# miles = JackRussellTerrier("Miles", 4)

# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)

# # print(miles.species)
# # print(buddy.name)
# # print(jack)
# # print(jim.speak("Woff"))

# print(miles.speak())
# print(miles.speak("Grrr"))