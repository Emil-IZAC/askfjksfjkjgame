class Player:
    inventory = []
    def __init__(self, hp, xp, gold):
        self.hp = hp
        self.xp = xp
        self.gold = gold
        self.maxHp = hp
        self.level = 0
        self.maxXp = 30
        self.location = 0

class Location:
    def __init__(self, name, index, availableLocationsIndexList, npcList, objectList, enemyList):
        self.name = name
        self.index = index
        self.availableLocationsIndexList = availableLocationsIndexList
        self.npcList = npcList
        self.objectList = objectList
        self.enemyList = enemyList
        self.description = ""

class NPC:
    def __init__(self, name):
        self.name = name

class Object:
    def __init__(self, name):
        self.name = name
    
    def use(self):
        pass

class Weapon(Object):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def use(self):
        print("using weapon")

class Potion(Object):
    def __init__(self, name, healPoints):
        self.name = name
        self.healPoints = healPoints
    
    def use(self):
        print("using potion")

class Enemy:
    def __init__(self, name, hp, xpReward, goldReward):
        self.name = name
        self.hp = hp
        self.xpReward = xpReward
        self.goldReward = goldReward
        self.maxHp = hp

player = Player(20, 0, 5)

location1 = Location("forest entrance", 0, [1], [NPC("Maurice")], [], [])
location1.description = "\nYou find yourself at the entrance of the Darkwood forest, a bearded man waves his arm at you. What do you do?\n"
location2 = Location("forest", 1, [0, 2, 3], [], [], [Enemy("Wolf", 5, 10, 2), Enemy("Ghost", 4, 8, 3)])
location2.description = "\nYou find yourself deep into the Darkwood forest, a few evil creatures populate the place. What do you do?\n"
location3 = Location("glade", 2, [1], [], [Potion("mega health potion", 20)], [])
location3.description = "\nYou find yourself in an isolated glade, with an empty well in the middle. Something shiny catches your eye on the side of the well. What do you do?\n"
location4 = Location("village", 3, [1, 4], [NPC("Eugene"), NPC("Bernard")], [Potion("health potion", 10)], [])
location4.description = "\nYou find yourself in a small village full of townspeople greeting you. What do you do?\n"
location5 = Location("dungeon entrance", 4, [3, 5], [], [Potion("health potion", 10)], [Enemy("Evil Wizard", 10, 20, 8)])
location5.description = "\nYou find yourself at the entrance of the Darkwood dungeon, a few menacing creatures guard the way. What do you do?\n"
location6 = Location("dungeon", 5, [4], [], [], [Enemy("Slime Blob", 20, 15, 10), Enemy("Giant Spider", 12, 25, 15), Enemy("Zombie", 15, 18, 12), Enemy("Dragon", 50, 50, 50)])
location6.description = "\nYou find yourself deep inside the Darkwood dungeon, many creatures threatening to attack you. What do you do?\n"
locations = [location1, location2, location3, location4, location5, location6]

inCombat = False
hasGameEnded = False
while hasGameEnded == False:
    print("------------------------------------------------------------------------------")
    currentLocation = locations[player.location]
    print(currentLocation.description)
    print("Health: " + str(player.hp) + "/" + str(player.maxHp) + "\nExperience: " + str(player.xp) + "/" + str(player.maxXp) + " (level " + str(player.level) + ")\nGold: " + str(player.gold) + " coins\n")
    
    if inCombat:
        print("fighting: ")
        playerInput = input()
        if playerInput == "f":
            hasGameEnded = True
        elif playerInput == "":
            print("something")
        else:
            print("invalid input")
    else:
        number = 0
        locationInputs = []
        npcInputs = []
        objectInputs = []
        enemyInputs = []
        print("Available locations:\n")
        for i in range(len(currentLocation.availableLocationsIndexList)):
            print("- " + locations[currentLocation.availableLocationsIndexList[i]].name + " : \"" + str(i) + "\"")
            locationInputs.append(str(i))
        number += len(currentLocation.availableLocationsIndexList)
        if len(currentLocation.npcList) != 0:
            print("\nAvailable NPCs:\n")
            for i in range(len(currentLocation.npcList)):
                print("- " + currentLocation.npcList[i].name + " : \"" + str(i + number) + "\"")
                npcInputs.append(str(i + number))
        number += len(currentLocation.npcList)
        if len(currentLocation.objectList) != 0:
            print("\nAvailable objects:\n")
            for i in range(len(currentLocation.objectList)):
                print("- " + currentLocation.objectList[i].name + " : \"" + str(i + number) + "\"")
                objectInputs.append(str(i + number))
        number += len(currentLocation.objectList)
        if len(currentLocation.enemyList) != 0:
            print("\nAvailable enemies:\n")
            for i in range(len(currentLocation.enemyList)):
                print("- " + currentLocation.enemyList[i].name + " : \"" + str(i + number) + "\"")
                enemyInputs.append(str(i + number))
        print("\nOther actions:\n\n- quit game : \"f\"\n")
        playerInput = input()
        if playerInput == "f":
            hasGameEnded = True
        elif playerInput in locationInputs:
            player.location = currentLocation.availableLocationsIndexList[int(playerInput)]
        elif playerInput in npcInputs:
            print("talk to npc")
        elif playerInput in objectInputs:
            print("pick up object")
        elif playerInput in enemyInputs:
            print("fight enemy")
        else:
            print("invalid input")