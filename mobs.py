#enemies list
import random

class QuillRat():
    #mob = quill_rat()
    #mob.print_details()
    health = 40
    attack = random.randint(0,16)
    location = "swamp"
    name = "Quill Rat"
    attack1 = "bite"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))


class Zombie():
    #mob = quill_rat()
    #mob.print_details()
    health = 40
    attack = random.randint(0,16)
    location = "cave"
    name = "Zombie"
    attack1 = "smack"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class MonsterGenerator():
    def __init__(self):
        self.monster_list = []
        self.location_map = {}
    def generate_list(self):
        self.monster_list.append(QuillRat()) #manually adding monsters to monster list
        self.monster_list.append(Zombie())

    def generate_location_list(self):
        self.location_map["cave"] = Zombie()
        self.location_map["swamp"] = QuillRat()

    def pick_monster1(self):
        return self.monster_list[random.randint(0,len(self.monster_list))] #randomly picks monster from above list

    def pick_monster2(self, location):
        output = []
        for monster in self.monster_list:
          if monster.location == location:
            output.append(monster)

        return output

        return self.location_map[location]
