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



