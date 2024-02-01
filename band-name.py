from data import city_names, names
import random

computer_place = random.choice(city_names)
computer_name = random.choice(names)

print("Welcome to the Band Name Generator.")
print("Enter the name of a city, town or village: ")
place = input()
print("Enter the name of your pet, real or imagined: ")
pet = input()
print("Your band name could be " + place + " " + pet)
print(f"My band is called {computer_place} {computer_name}!")
