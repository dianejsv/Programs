import pyfiglet
from colorama import Fore
import time

name = input("Enter your Name: ")
dream_job = input("What's your dream job? ")

fancy_text_name = pyfiglet.figlet_format(name, font="doom")
fancy_text_dream_job = pyfiglet.figlet_format(dream_job, font="starwars")

colored_fancy_name = Fore.LIGHTCYAN_EX + fancy_text_name + Fore.RESET
colored_fancy_dream_job = Fore.LIGHTMAGENTA_EX + fancy_text_dream_job + Fore.RESET

print("My names is: ", end='')
for char in colored_fancy_name:
    print(char, end='', flush=True)
    time.sleep(0.01)

print("\nMy dream job is: ", end='')
for char in colored_fancy_dream_job:
    print(char, end='', flush=True)
    time.sleep(0.01)

print("Thank you!")
