import random

class Character():
    health = 100
    attack = random.randint(1,7)
    name = "Hero"
    attack1 = "punch"
    attack2 = "kick"
    inventory = {"Health Potion": 1, "Sword": 1, "Scroll of Town Portal": 1}
    character_level = 1
    character_exp = 0
    


    def print_details(self):
       print("You respond to the monster by attacking with {}.  You did {} damage.".format(self.attack1, self.attack))
