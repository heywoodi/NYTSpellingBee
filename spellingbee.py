import json
import os
import time
import math
import itertools
from pyautogui import typewrite, press
from time import sleep


LETTERS = ""


os.system('cls' if os.name == 'nt' else 'clear')
with open("dict.json", "r") as read_file:
    data = json.load(read_file)
dictionary = [i.upper() for i in data["words"]]
if LETTERS:
    valid = LETTERS
else:
    input("What are todays letterboxd letters? ").upper()
ALPHABET = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
invalid = [i for i in ALPHABET if i not in list(valid)]#gather invalid letters
dictionary = [i for i in dictionary if all(c not in i for c in invalid)]#remove words with invalid letters
dictionary = [i for i in dictionary if valid[0] in i ]#make sure words contain the central letter
pangrams = [i for i in dictionary if all(c in i for c in valid)]#find the words that are pangrams
dictionary = [i for i in dictionary if i not in pangrams]#remove pangrams from origional list
dictionary = [i for i in dictionary if (len(i) >= 4)]#remove words with 3 or less letters
dictionary.sort(key=len)
pangrams.sort(key=len)

print(dictionary)
print(pangrams)

#sleep(4)
#for n in pangrams:
#    sleep(1)
#    typewrite(n)
#    press('enter')
#for n in dictionary:
#    sleep(1)
#    typewrite(n)
#    press('enter')
