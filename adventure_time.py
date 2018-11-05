import random, time, sys
from mobs import QuillRat, Zombie, MonsterGenerator

damage = 10
health = 100
#You want to instantiate the mob/enemy here like below
mob = MonsterGenerator()
mob.generate_list()
mob.generate_location_list()

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

#print(start)
#print(quill_rat.print_details())

attack(mob.pick_monster1())
attack(mob.pick_monster2("cave"))

#create list and randomly select from the list to choose which monster to fight
