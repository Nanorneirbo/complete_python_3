import random


class Enemy:
    atk_l = 60
    atk_h = 80

    def get_atk(self):
        print(self.atk_l)

enemy1 = Enemy()
enemy1.get_atk()
