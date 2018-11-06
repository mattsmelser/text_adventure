import random, time, sys
from mobs import QuillRat, Zombie, MonsterGenerator
from char import Character
from items import items

damage = 10
health = 100
#You want to instantiate the mob/enemy here like below
mob = MonsterGenerator()
mob.generate_list()
mob.generate_location_list()
char = Character

def attack(mob):
    # then do something like this
    # mob.print_details()
    mob.print_details()

def attack(char):
    char.print_details()

def display_intro():
    print("Welcome traveler, you have arrived in The Rogue Encampment with the ultimate goal of reaching The Catacombs.")
    print("Best of luck on your adventure.")

def start():
    print("display_intro()")
    print("On your way out of town, you see a hostile quill rat.")




attack(mob.pick_monster()) #(this one works, commenting it out for testing)
#attack(mob.pick_monster2("Blood Moor"))
#attack(mob.pick_monster3)
attack(char())

#create list and randomly select from the list to choose which monster to fight
