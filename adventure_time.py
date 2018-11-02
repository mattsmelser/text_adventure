import random, time, sys
from mobs import QuillRat#, zombie

damage = 10
health = 100
#You want to instantiate the mob/enemy here like below
mob = QuillRat()  #Instantiate the quill_rat class, now mob is a quill_rat

def attack(mob):
    # then do something like this
    # mob.print_details()
    mob.print_details()

def display_intro():
    print("Welcome traveler, you have arrived in The Rogue Encampment with the ultimate goal of reaching The Catacombs.")
    print("Best of luck on your adventure.")

def start():
    print("display_intro()")
    print("On your way out of town, you see a hostile quill rat.")

def character():
    pass

print(start)
#print(quill_rat.print_details())

attack(mob)
