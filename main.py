import sys
from models import *
from exceptions import *
import settings


def start_name():
    while True:
        user_name = input("Welcome! Enter your name: ")
        if len(user_name) < 2:
            print("You must enter a name more than three letters. Try again:")
        elif user_name == "":
            print("You didn't enter your name: Another try: ")
        else:
            break
    return user_name


def play(user_name):
    print("""
        The wizard defeats the warrior,
        The warrior defeats the robber,
        The robber defeats the wizard.
        
        For a successful attack, the enemy loses one life,
        for defeating the enemy, you get 5 points.
        Good Game Have Fun.
    """)
    player = Player(user_name)
    level = settings.player_level
    enemy = Enemy(level)
    while True:
        try:
            print(player.attack(enemy))
            print(player.defence(enemy))
        except EnemyDown:
            print("Enemy defeated. Next!")
            level += 1
            enemy = Enemy(level)
            player.score += 5
            print(user_name, "Lives - ", player.lives)
            print("Enemy level - ", enemy.get_info())
            continue


def process_game(name):
    try:
        play(name)
    except GameOver:
        print("Game over!")
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")


if __name__ == "__main__":
    try:
        name = start_name()
        print("Hello, ", name, ", you started the program.")
        print("You can enter 'start' to start game or 'help' for more command.")
        while True:
            user_input = input("Enter command: ")
            if user_input == "start":
                process_game(name)
            elif user_input == "show scores":
                    GameOver.show.scores()
            elif user_input == "help":
                for i in settings.display_help:
                    print(i)
            elif user_input == "exit":
                sys.exit()
            else:
                print("Incorrect command: ")
    finally:
        print("Close program...")
        print("See you!")
