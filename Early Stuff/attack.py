import random


player_hp = 260
enemy_atk_low = 60
enemy_atk_high = 80

while player_hp > 0:
    damage = random.randrange(enemy_atk_low, enemy_atk_high)
    player_hp = player_hp-damage

    if player_hp <= 30:
        player_hp = 30

    print("Enemy strikes for", damage, "points of damage. Current HP is", player_hp)

    if player_hp == 30:
        print("You have low health you have been teleported to nearest inn")
        break


