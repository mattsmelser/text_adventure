#enemies list
import random

class QuillRat():
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

class Ghost():
    health = random.randint(9,15)
    attack = random.randint(2,7)
    experience = 44
    name = "Ghost"
    attack1 = "ghostly essence"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class Spider():
    health = random.randint(12,20)
    attack = random.randint(5,17)
    experience = 57
    name = "Giant Spider"
    attack1 = "venomous bite"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class CaveSpider():
    health = random.randint(12,20)
    attack = random.randint(5,17)
    experience = 57
    name = "Cave Spider"
    attack1 = "venomous bite"
    def print_details(self):
       print("You encounter a {}.  It has {} health and it attacks you with {} doing {} damage.".format(self.name, self.health, self.attack1, self.attack))

class MonsterGenerator():
    def __init__(self):
        self.monster_list = []
        self.location_map = {}
    def generate_list(self):
        self.monster_list.append(QuillRat()) #manually adding monsters to monster list
        self.monster_list.append(Zombie())
        self.monster_list.append(Skeleton())
        self.monster_list.append(Ghost())
        self.monster_list.append(Spider())
        self.monster_list.append(CaveSpider())
    def pick_monster(self):
        return self.monster_list[random.randint(0,(len(self.monster_list)-1))] #randomly picks monster from above list
        #changed the list to len(self.monster_list)-1, for some reason it was still able to grab the max number and throwing an error

    def generate_location_list(self):
        self.location_map["Blood Moor"] = Zombie(), QuillRat()
        self.location_map["Den Of Evil"] = QuillRat(), Skeleton(), Zombie()
        self.location_map["Cold Plains"] = Skeleton(), Zombie(), QuillRat()
        self.location_map["Cave Level 1"] = CaveSpider()
        self.location_map["Cave Level 2"] = CaveSpider()
        self.location_map["Stony Field"] = Spider(), Skeleton(), Zombie(), Ghost()
        #print(self.location_map)

    def pick_monster2(self, location):
        output = []
        for local in location:
            if self.location_map == location:
                #print (self.location_map)
                monster = self.location_map[random.randint(0,(len(self.location_map)-1))]
                output.append(monster)
        return output
        return self.locaiton_map[location]


    def pick_monster3(self, location):
        output = []
        for monster in self.monster_list:
          if monster.location == location:
            output.append(monster)

        return output

        return self.location_map[location]
