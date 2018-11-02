#enemies list
import random

class QuillRat():
    #mob = quill_rat()
    #mob.print_details()
    health = 40
    attack = random.randint(0,16)
    name = "Quill Rat"
    attack1 = "bite"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))


class Zombie():
    #mob = quill_rat()
    #mob.print_details()
    health = 40
    attack = random.randint(0,16)
    name = "Zombie"
    attack1 = "smack"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class MonsterGenerator():
    def __init__(self):
        self.monster_list = []
    def generate_list(self):
        self.monster_list.append(QuillRat()) #manually adding monsters to monster list
        self.monster_list.append(Zombie())
    def pick_monster(self):
        return self.monster_list[random.randint(0,len(self.monster_list))] #randomly picks monster from above list
