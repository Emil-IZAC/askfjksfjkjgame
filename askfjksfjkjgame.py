import random

class Player:
    def __init__(self, hp, xp, gold):
        self.hp = hp
        self.xp = xp
        self.gold = gold
        self.maxHp = hp
        self.level = 0
        self.maxXp = 20
        self.location = 0
        self.fightingEnemy = None
        self.weapons = []
        self.potions = []
        self.talkingNPC = None

    def Heal(self, hp):
        self.hp += hp
        if self.hp > self.maxHp:
            self.hp = self.maxHp
    
    def Hit(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

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
        self.sentence = ""
        self.interactions = []
        self.postInteractions = []
        self.interactionCount = 0
        self.hasTalked = False

class Interaction:
    def __init__(self, answers, responses):
        self.answers = answers
        self.responses = responses

class Object:
    def __init__(self, name):
        self.name = name
    
    def Use(self):
        pass

class Weapon(Object):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def Use(self):
        print("using weapon")

class Potion(Object):
    def __init__(self, name, healPoints):
        self.name = name
        self.healPoints = healPoints
    
    def Use(self):
        print("using potion")

class Enemy:
    def __init__(self, name, hp, xpReward, goldReward, damage, hitProbability, flavorText):
        self.name = name
        self.hp = hp
        self.xpReward = xpReward
        self.goldReward = goldReward
        self.maxHp = hp
        self.flavorText = flavorText
        self.damage = damage
        self.hitProbability = hitProbability
    
    def Heal(self, hp):
        self.hp += hp
        if self.hp > self.maxHp:
            self.hp = self.maxHp
    
    def Hit(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

player = Player(20, 0, 5)
player.weapons = [Weapon("fist", 1)]

location1 = Location("forest entrance", 0, [1], [NPC("Maurice")], [], [])
location1.description = "\nYou find yourself at the entrance of the Darkwood forest, a bearded man waves his arm at you. What do you do?\n"
location2 = Location("forest", 1, [0, 2, 3], [], [], [Enemy("Wolf", 5, 10, 2, 3, 0.75, "\"GRRRRRRRR\""), Enemy("Ghost", 4, 8, 3, 2, 0.6, "\"boo\"")])
location2.description = "\nYou find yourself deep into the Darkwood forest, a few evil creatures populate the place. What do you do?\n"
location3 = Location("glade", 2, [1], [], [Potion("mega health potion", 20)], [])
location3.description = "\nYou find yourself in an isolated glade, with an empty well in the middle. Something shiny catches your eye on the side of the well. What do you do?\n"
location4 = Location("village", 3, [1, 4], [NPC("Eugene"), NPC("Bernard")], [Potion("health potion", 10)], [])
location4.description = "\nYou find yourself in a small village full of townspeople greeting you. What do you do?\n"
location5 = Location("dungeon entrance", 4, [3, 5], [], [Potion("health potion", 10)], [Enemy("Evil Wizard", 10, 20, 8, 5, 0.8, "\"wawa I am here to steal your beans\"")])
location5.description = "\nYou find yourself at the entrance of the Darkwood dungeon, a few menacing creatures guard the way. What do you do?\n"
location6 = Location("dungeon", 5, [4], [], [], [Enemy("Slime Blob", 20, 15, 10, 8, 0.5, "\"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\""), Enemy("Giant Spider", 12, 25, 15, 6, 0.9, "\"Ah, fresh blood, I had been waiting for this\""), Enemy("Zombie", 15, 18, 12, 7, 0.55, "\"Greetings fellow humanoid, I bid you farewell as I must consume the flesh on your person\""), Enemy("Dragon", 50, 50, 50, 10, 0.8, "Muahahahah >:)")])
location6.description = "\nYou find yourself deep inside the Darkwood dungeon, many creatures threatening to attack you. What do you do?\n"
locations = [location1, location2, location3, location4, location5, location6]

location1.npcList[0].sentence = "\"Hey there young traveler, what brings you here?\"\n"
location1.npcList[0].interactions.append(Interaction(["\"I want to explore this forest\"", "\"I don't know, I got lost\"", "\"I don't need your help, get out of my way!\""], ["\"Well, you'll need this sword to explore safely! Many dangers lie ahead...\"\n", "\"Oh, well if you're going in anyway, be careful, here's a sword to help you fight!\"\n", "\"Very well, good luck and don't die!\"", 0]))
location1.npcList[0].interactions.append(Interaction(["\"Wow, thanks!\" (+1 sword)", "\"I don't need it\""], ["\"You're welcome! Please return it to me when you're finished however, this sword is very important to me.\"\n", 1, "\"Ah, well in that case good luck and don't die!\"\n"]))
location1.npcList[0].postInteractions.append(Interaction(["Yes (quit game)", "No"], ["Goodbye adventurer!\n", -1, "Ah, good luck out there then!\n"]))

location4.npcList[0].sentence = "\"Greetings fellow adventurer, looks like you're badly injured! I have potions to sell if you're interested!\nOnly 10 gold pieces for a health potion (+10 hp), and 18 gold pieces for a mega health potion! (+20 hp)\"\n"
location4.npcList[0].interactions.append(Interaction(["\"I'll take one health potion!\"", "\"I'll take one mega health potion!\"", "\"I'm good, thanks!\""], ["\"Anything else?\"\n", 2, "\"Anything else?\"\n", 3, "\"No problem, stop by anytime!\"", 0]))

location4.npcList[1].sentence = "\"My dad was a famous adventurer, and he got killed by the dragon in that cave... You'll never be as strong as him, I think you should leave. You'll never beat this dragon, trust me.\"\n"
location4.npcList[1].interactions.append(Interaction(["\"I don't care for you threats, I can do this!\"", "\"If I beat the dragon, I'm your new dad, deal?\""], ["\"Ok, knock yourself out\"\n", "\"Deal. You'll never beat him anyway\"\n"]))

inCombat = False
inDialogue = False
hasGameEnded = False
while hasGameEnded == False:
    
    currentLocation = locations[player.location]
    
    print("Health: " + str(player.hp) + "/" + str(player.maxHp) + "\nExperience: " + str(player.xp) + "/" + str(player.maxXp) + " (level " + str(player.level) + ")\nGold: " + str(player.gold) + " coins\n")
    
    if inCombat:
        print("fighting: " + player.fightingEnemy.name)
        print("Health: " + str(player.fightingEnemy.hp) + "/" + str(player.fightingEnemy.maxHp) + "\n")
        number = 0
        weaponInputs = []
        potionInputs = []
        print("Available Weapons:\n")
        for i in range(len(player.weapons)):
            print("- " + player.weapons[i].name + " ; " + str(player.weapons[i].damage) + " dmg : \"" + str(i) + "\"\n")
            weaponInputs.append(str(i))
        number += len(player.weapons)
        if len(player.potions) > 0:
            print("Available Potions:\n")
            for i in range(len(player.potions)):
                print("- " + player.potions[i].name + " ; +" + str(player.potions[i].healPoints) + " hp : \"" + str(i + number) + "\"\n")
                potionInputs.append(str(i + number))
        print("\nOther actions:\n\n- escape combat (50% chance) : \"e\"\n\n- quit game : \"f\"\n")
        playerInput = input("your input: ")
        print("------------------------------------------------------------------------------")
        if playerInput == "f":
            hasGameEnded = True
        elif playerInput == "e":
            print("You attempt to flee")
            if random.randint(0, 1) == 1:
                print("You fail\n")
            else:
                print("You succeed\n")
                inCombat = False
        elif playerInput in weaponInputs:
            player.fightingEnemy.Hit(player.weapons[int(playerInput)].damage)
            print("You attack the " + player.fightingEnemy.name + " with your " + player.weapons[int(playerInput)].name + "!\n")
            if player.fightingEnemy.hp == 0:
                print("The " + player.fightingEnemy.name + " has been slain!\n")
                print("+" + str(player.fightingEnemy.xpReward) + " xp\n+" + str(player.fightingEnemy.goldReward) + " coins\n")
                player.xp += player.fightingEnemy.xpReward
                player.gold += player.fightingEnemy.goldReward
                inCombat = False
                if player.xp >= player.maxXp:
                    player.xp -= player.maxXp
                    player.level += 1
                    print("You've reached level " + str(player.level) + "! Your health has been refilled\n+10 max hp\n+10 gold\n")
                    player.maxHp += 10
                    player.hp = player.maxHp
                    player.gold += 10
        elif playerInput in potionInputs:
            player.Heal(player.potions[int(playerInput) - len(player.weapons)].healPoints)
            print("You drink your " + player.potions[int(playerInput) - len(player.weapons)].name + " and heal " + str(player.potions[int(playerInput) - len(player.weapons)].healPoints) + " hp!\n")
            player.potions.pop(int(playerInput) - len(player.weapons))
        else:
            print("invalid input")
        
        if inCombat:
            print("The " + player.fightingEnemy.name + " attacks:\n")
            if random.randint(0, 100) < player.fightingEnemy.hitProbability * 100:
                print("You take " + str(player.fightingEnemy.damage) + " points of damage!\n")
                player.Hit(player.fightingEnemy.damage)
                if player.hp == 0:
                    print("You were slain...")
                    hasGameEnded = True
            else:
                print("It misses!\n")


    elif inDialogue:
        correctInteractions = player.talkingNPC.interactions
        if player.talkingNPC.hasTalked:
            correctInteractions = player.talkingNPC.postInteractions
        print("Talking to :" + player.talkingNPC.name + "\n")
        answerInputs = []
        if player.talkingNPC.interactionCount == 0:
            print(player.talkingNPC.sentence)
        for i in range(len(correctInteractions[player.talkingNPC.interactionCount].answers)):
            print("- " + correctInteractions[player.talkingNPC.interactionCount].answers[i] + " : \"" + str(i) + "\"")
            answerInputs.append(str(i))
        playerInput = input("your input: ")
        print("------------------------------------------------------------------------------")
        if playerInput == "f":
            hasGameEnded = True
        elif playerInput in answerInputs:
            numbersOffset = 0
            responsesIterator = 0
            while responsesIterator - numbersOffset <= int(playerInput):
                if type(correctInteractions[player.talkingNPC.interactionCount].responses[responsesIterator]) == int:
                    numbersOffset += 1
                responsesIterator += 1
            print(correctInteractions[player.talkingNPC.interactionCount].responses[int(playerInput) + numbersOffset])
            if len(correctInteractions[player.talkingNPC.interactionCount].responses) > int(playerInput) + numbersOffset + 1:
                if type(correctInteractions[player.talkingNPC.interactionCount].responses[int(playerInput) + numbersOffset + 1]) == int:
                    specialNumber = correctInteractions[player.talkingNPC.interactionCount].responses[int(playerInput) + numbersOffset + 1]
                    if specialNumber == -1:
                        hasGameEnded = True
                    elif specialNumber == 0:
                        inDialogue = False
                    elif specialNumber == 1:
                        print("You now have a sword! (3 dmg)\n")
                        player.weapons.append(Weapon("Sword", 3))
                    elif specialNumber == 2:
                        if player.gold >= 10:
                            print("You now have a potion! (+10 hp)\n")
                            player.potions.append(Potion("health potion", 10))
                            player.gold -= 10
                        else:
                            print("You don't have enough gold to buy this!\n")
                    elif specialNumber == 3:
                        if player.gold >= 20:
                            print("You now have a mega potion! (+20 hp)\n")
                            player.potions.append(Potion("mega health potion", 20))
                            player.gold -= 20
                        else:
                            print("You don't have enough gold to buy this!\n")
            player.talkingNPC.interactionCount += 1
            if player.talkingNPC.interactionCount > len(correctInteractions) - 1:
                inDialogue = False
                player.talkingNPC.interactionCount = 0

                if player.talkingNPC.name == "Maurice": #very hacky but whatever
                    player.talkingNPC.sentence = "Hey there young traveler, ready to leave?\n"
                    player.talkingNPC.hasTalked = True
        else:
            print("invalid input")


    else:
        print(currentLocation.description)
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
        playerInput = input("your input: ")
        print("------------------------------------------------------------------------------")
        if playerInput == "f":
            hasGameEnded = True
        elif playerInput in locationInputs:
            player.location = currentLocation.availableLocationsIndexList[int(playerInput)]
        elif playerInput in npcInputs:
            inDialogue = True
            player.talkingNPC = currentLocation.npcList[int(playerInput) - len(currentLocation.availableLocationsIndexList)]
        elif playerInput in objectInputs:
            player.potions.append(currentLocation.objectList[int(playerInput) - len(currentLocation.availableLocationsIndexList) - len(currentLocation.npcList)])
            print(str(int(playerInput) - len(currentLocation.availableLocationsIndexList) - len(currentLocation.npcList)))
            print("You pick up the " + currentLocation.objectList[int(playerInput) - len(currentLocation.availableLocationsIndexList) - len(currentLocation.npcList)].name + "!\n")
            currentLocation.objectList.pop(int(playerInput) - len(currentLocation.availableLocationsIndexList) - len(currentLocation.npcList))
        elif playerInput in enemyInputs:
            inCombat = True
            player.fightingEnemy = currentLocation.enemyList[int(playerInput) - len(currentLocation.availableLocationsIndexList) - len(currentLocation.npcList) - len(currentLocation.objectList)]
            print("You approach the " + player.fightingEnemy.name)
            print(player.fightingEnemy.flavorText)
            currentLocation.enemyList.pop(int(playerInput) - len(currentLocation.availableLocationsIndexList) - len(currentLocation.npcList) - len(currentLocation.objectList))
        else:
            print("invalid input")