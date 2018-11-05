#enemies list
import random

class QuillRat():
    #mob = quill_rat()
    #mob.print_details()
    health = random.randint(1,6)
    attack = random.randint(0,3)
    experience = 21
    name = "Quill Rat"
    attack1 = "bite"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class Zombie():
    health = random.randint(7,13)
    attack = random.randint(2,4)
    experience = 33
    name = "Zombie"
    attack1 = "smack"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class Skeleton():
    health = random.randint(7,12)
    attack = random.randint(1,4)
    experience = 34
    name = "Skeleton"
    attack1 = "its sword"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class MonsterGenerator():
    def __init__(self):
        self.monster_list = []
    def generate_list(self):
        self.monster_list.append(QuillRat()) #manually adding monsters to monster list
        self.monster_list.append(Zombie())
        self.monster_list.append(Skeleton())
    def pick_monster(self):
        return self.monster_list[random.randint(0,len(self.monster_list))] #randomly picks monster from above list
        #I am getting an error of "list index out of range" for the above line when I run the program about 1/4 of the time.  
        #I'm not sure what number is rolling, because it should be 0, 1, or 2 that all point to something in the monster_list
