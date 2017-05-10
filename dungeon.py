import random

hero = "@"
hero_x = 0
level = "..a.b.G.p.E.b..$K..r.$.h..c...D...."
level = list(level)
hunger = 0
money = 0
hp=10
#        key :   name   hunger hp
food = {"a":("apple",5,0),
        "b":("banana",6,2),
        "p":("pork",9,0),
        "r":("rotten meat",4,-2),
        "c":("cake",17,0),
        "h":("big health potion",0,42)}
#            key  name  chance to hit you, chance to evade,   max damage to you
monsters = {"G":("Dog",0.4,0.35,3),
            "D":("Dragon",0.25,0.1,22),
            "E":("Evil Ducks",0.47,0.23,2),
            "K":("Kobolds",0.8,0.01,1)}
while hp > 0:
    for x, char in enumerate(level):
        if x == hero_x:
            print(hero, end="")
        else:
            print(char, end="")
    print()
    hunger += 1
    command=input("Hunger: {} Money: {} HP: {},your command?".format(hunger, money, hp))
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
    stuff = level[hero_x]
    if stuff in food:
        print("You eat : ", food[stuff][0])
        hunger -= food[stuff][1]
        hp += food[stuff][2]
        level[hero_x] = "."
    elif stuff == "$":
        print("You found money!")
        money += random.randint(1, 20)
        level[hero_x] = "."
    elif stuff in monsters:
        print("You fight : ", monsters[stuff][0])
        hunger += monsters[stuff][1]
        hp -= monsters[stuff][2]
        level[hero_x] = "."
