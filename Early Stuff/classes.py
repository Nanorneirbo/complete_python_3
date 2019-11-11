import random


class Enemy:
    hp = 200

    def __init__(self, atk_l, atk_h):
        self.atk_l = atk_l
        self.atk_h = atk_h

    def get_atk(self):
        print(self.atk_l)

    def get_hp(self):
        print(("Hp is", self.hp))


enemy1 = Enemy(40, 49)
enemy1.get_atk()
enemy1.get_hp()

enemy2 = Enemy(75, 90)
enemy2.get_atk()
enemy2.get_hp()

