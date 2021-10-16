import random
from exceptions import *
import settings


class Enemy:

    def __init__(self, level):
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown

    def get_info(self):
        return self.lives


class Player:
    def __init__(self, name):
        self.name = name

    score = 0
    lives = settings.player_lives
    allowed_attacks = [1, 2, 3]

    @staticmethod
    def fight(attack, defense) -> int:
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or (attack == 3 and defense == 1):
            return 1
        elif (attack == 1 and defense == 3) or (attack == 2 and defense == 1) or (attack == 3 and defense == 2):
            return -1
        else:
            return 0

    @staticmethod
    def input_validation(text_var: str) -> int:
        while True:
            num = input(text_var)
            if num == '1':
                return 1
            elif num == '2':
                return 2
            elif num == '3':
                return 3
            else:
                print("Input is incorrect")

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.score, self.name)

    def attack(self, enemy_obj):
        attack_player = Player.input_validation("Select attack: ")
        res = self.fight(attack_player, enemy_obj.select_attack())
        if res == 0:
            return "It's a draw!"
        elif res == -1:
            return "You missed!"
        else:
            enemy_obj.decrease_lives()
            return "You attacked successfully!"

    def defence(self, enemy_obj):
        defence_player = Player.input_validation("Select defence: ")
        res = self.fight(enemy_obj.select_attack(), defence_player)
        if res == 0:
            return "It's a draw!"
        elif res == -1:
            return "He missed!"
        else:
            self.decrease_lives()
            return "His attack successfully!"