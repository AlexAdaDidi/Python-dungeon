import random

hero = "@"
hero_x = 0
level = "..a.b..p..b..$..r.$...P...S...."
level = list(level)
hunger = 0
money = 0
hp=10
while hp > 0:
    for x, char in enumerate(level):
        if x == hero_x:
            print(hero, end="")
        else:
            print(char, end="")
    print()
    hunger += 1
    command=input("Hunger: {} Money: {} ,your command?".format(hunger, money))
    if command == "quit" or command == "exit":
        break
    elif command == "a":
        hero_x -= 1
    elif command == "d":
        hero_x += 1
    elif command == "D":
        hero_x += 2
    elif command == "A":
        hero_x -= 2
    elif command == "superjump":
        hero_x += 10
    elif command == "superbackjump":
        hero_x -= 10
    elif command == "randomjump":
        hero_x = random.randint(-10, 10)
    # ----------Auswertung----------
    if level[hero_x] == "a":
        print("You eat an apple.")
        hunger -= 5
        level[hero_x] = "."
    elif level[hero_x] == "b":
        print("You eat a banana.")
        hunger -= 6
        level[hero_x] = "."
    elif level[hero_x] == "p":
        print("Such a good pork.")
        hunger -= 9
        level[hero_x] = "."
    elif level[hero_x] == "P":
        print("Yummy pie!")
        hunger -= 17
        level[hero_x] = "."
    elif level[hero_x] == "r":
        print("Bäh! Rotten meat!")
        hunger -= 4
        hp -= 2
        level[hero_x] = "."
    elif level[hero_x] == "$":
        print("You found money!")
        money += random.randint(1, 20)
        level[hero_x] = "."
