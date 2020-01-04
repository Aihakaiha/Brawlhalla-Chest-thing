import time



chests = [["Celestial", 18,["Seraph Artemis", "The Korinthian", "Emperor Koji"]], 
    ["Royal Order", 18,["Gentleman Wu Shang", "Admiral Isaiah", "Madame Yumiko"]], 
    ["Ragnarök", 18,["Fenrir Mordex", "Nidhogg Nai", "Jotun Ulgrim"]],
    ["Sunken", 18,["Atlantean Ada", "Deep Depths Ragnir", "Dreadnought Lucien"]],
    ["Imperial", 18,["Yakuza Koji", "Death Adder Hattori", "Warrior Spirit Kor"]],
    ["Skysail",18,["Sky Scourge Azoth", "Corsair Orion", "Airship Orion"]],
    ["Olympian", 18,["Athena Kaya", "Chimera Val", "Poseidon Thatch"]],
    ["Ancient", 18,["Fangwild Fawn Ember", "Winged Serpent Nai", "White Fang Gnash"]],
    ["Sandstorm", 18,["Anubis Mirage", "Amun-Raza", "God King Teros"]],
    ["Forbidden",18,["Harpy Brynn", "Draugr Bödvar", "Shadowlord Cross"]],
    ["Outlaw",18,["Aces High Caspian", "Sidewinder Hattori", "Badlands Asuri"]],
    ["Brawl City",18,["Nix Couture", "New School Jhala", "Crossfade Orion"]],
    ["Dragon", 18,["Lord Sentinel", "Elven Ranger Diana", "Dragonslayer Val"]],
    ["Wild", 18,["Meadowguard Ember", "Lionheart Roland", "Fox Spirit Yumiko"]],
    ["Odin's", 18,["Warchief Bödvar", "Forgeheart Teros"]],
    ["Elements", 18,["Dust Devil Cassidy", "Stormlord Ada", "Inferno Ragnir"]],
    ["Exalted", 18,["Silvermane Gnash", "Komainu Jiro", "Lionguard Diana"]],
    ["Synthwave", 18,["Overdrive Lucien", "Queen Beat Sidra", "Mad Dog Mordex"]]]


def chest_calculation():
    print("----------------------------------")
    print("|id   name            # of items")
    print("|---------------------------------")
    print("|0   |", chests[0][0], "    |  ", chests[0][1], "     |")
    print("|1   |", chests[1][0], "  |  ", chests[1][1], "     |")
    print("|2   |", chests[2][0], "     |  ", chests[2][1], "     |")
    print("|3   |", chests[3][0], "       |  ", chests[3][1], "     |")
    print("|4   |", chests[4][0], "     |  ", chests[4][1], "     |")
    print("|5   |", chests[5][0], "      |  ", chests[5][1], "     |")
    print("|6   |", chests[6][0], "     |  ", chests[6][1], "     |")
    print("|7   |", chests[7][0], "      |  ", chests[7][1], "     |")
    print("|8   |", chests[8][0], "    |  ", chests[8][1], "     |")
    print("|9   |", chests[9][0], "    |  ", chests[9][1], "     |")
    print("|10  |", chests[10][0], "       |  ", chests[10][1], "     |")
    print("|11  |", chests[11][0], "   |  ", chests[11][1], "     |")
    print("|12  |", chests[12][0], "       |  ", chests[12][1], "     |")
    print("|13  |", chests[13][0], "         |  ", chests[13][1], "     |")
    print("|14  |", chests[14][0], "       |  ", chests[14][1], "     |")
    print("|15  |", chests[15][0], "     |  ", chests[15][1], "     |")
    print("|16  |", chests[16][0], "      |  ", chests[16][1], "     |")
    print("|17  |", chests[17][0], "    |  ", chests[17][1], "     |")
    print("----------------------------------")
    pick_chest = input("Type chest ID: ")
    print("| Chest name: {}".format(chests[int(pick_chest)][0]))
    print("| Items in chest: {}".format(chests[int(pick_chest)][1]))
    owned_items = input("| How many items you own from the chest?: ")
    print("| Owned items: {}".format(owned_items))
    chest_content = chests[int(pick_chest)][1]
    true_cont = int(chest_content) - int(owned_items)
    print("| Locked items: {}".format(true_cont))
    chance = 1 / int(true_cont) * 100
    print("-----------------------------------")
    print("| Chance to get a specific skin: {}%".format(round(chance, 2)))
    print("-----------------------------------")
    chest_skins = chests[int(pick_chest)][2][0:3]
    print("-----------------------------------")
    print("| Chest exclusive skins: " + str(chest_skins))
    time.sleep(4)

def chest_content():  
    print("|id   name            Amount of items                                 Content")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("|0   |", chests[0][0], "    |  ", chests[0][1], "       |  ", chests[0][2][0], "      |   ", chests[0][2][1], "       |    ", chests[0][2][2], "         |")
    print("|--------------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|1   |", chests[1][0], "  |  ", chests[1][1], "       |  ", chests[1][2][0], "  |   ", chests[1][2][1], "       |    ", chests[1][2][2], "        |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|2   |", chests[2][0], "     |  ", chests[2][1], "       |  ", chests[2][2][0], "       |   ", chests[2][2][1], "          |    ", chests[2][2][2], "         |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|3   |", chests[3][0], "       |  ", chests[3][1], "       |  ", chests[3][2][0], "       |   ", chests[3][2][1], "   |    ", chests[3][2][2], "   |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|4   |", chests[4][0], "     |  ", chests[4][1], "       |  ", chests[4][2][0], "         |   ", chests[4][2][1], "  |    ", chests[4][2][2], "   |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|5   |", chests[5][0], "      |  ", chests[5][1], "       |  ", chests[5][2][0], "   |   ", chests[5][2][1], "        |    ", chests[5][2][2], "        |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|6   |", chests[6][0], "     |  ", chests[6][1], "       |  ", chests[6][2][0], "         |   ", chests[6][2][1], "          |    ", chests[6][2][2], "      |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|7   |", chests[7][0], "      |  ", chests[7][1], "       |  ", chests[7][2][0], " |   ", chests[7][2][1], "   |    ", chests[7][2][2], "     |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|8   |", chests[8][0], "    |  ", chests[8][1], "       |  ", chests[8][2][0], "       |   ", chests[8][2][1], "            |    ", chests[8][2][2], "       |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|9   |", chests[9][0], "    |  ", chests[9][1], "       |  ", chests[9][2][0], "         |   ", chests[9][2][1], "        |    ", chests[9][2][2], "     |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|10  |", chests[10][0], "       |  ", chests[10][1], "       |  ", chests[10][2][0], "   |   ", chests[10][2][1], "   |    ", chests[10][2][2], "       |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|11  |", chests[11][0], "   |  ", chests[11][1], "       |  ", chests[11][2][0], "         |   ", chests[11][2][1], "     |    ", chests[11][2][2], "      |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|12  |", chests[12][0], "       |  ", chests[12][1], "       |  ", chests[12][2][0], "       |   ", chests[12][2][1], "   |    ", chests[12][2][2], "     |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|13  |", chests[13][0], "         |  ", chests[13][1], "       |  ", chests[13][2][0], "   |   ", chests[13][2][1], "     |    ", chests[13][2][2], "    |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|14  |", chests[14][0], "       |  ", chests[14][1], "       |  ", chests[14][2][0], "     |   ", chests[14][2][1], "     |    ", "                      |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|15  |", chests[15][0], "     |  ", chests[15][1], "       |  ", chests[15][2][0], "  |   ", chests[15][2][1], "        |    ", chests[15][2][2], "       |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|16  |", chests[16][0], "      |  ", chests[16][1], "       |  ", chests[16][2][0], "    |   ", chests[16][2][1], "         |    ", chests[16][2][2], "      |")
    print("|----|---------------|-------------|------------------------|--------------------------|---------------------------|")
    print("|17  |", chests[17][0], "    |  ", chests[17][1], "       |  ", chests[17][2][0], "    |   ", chests[17][2][1], "     |    ", chests[17][2][2], "       |")
    print("-------------------------------------------------------------------------------------------------------------------")

while True:
    print("|ID       Command")
    print("|-------------------")
    print("|0        Calculation")
    print("|1        Content")
    print("|exit     Exit the program")
    print("|-------------------")
    w = input(" Input command ID: ")
    if w == "exit" or w == "Exit":
        exit()
    elif int(w) == 0:
        chest_calculation()
    elif int(w) == 1:
        chest_content()
    else:
        print(" Not Valid ID!")
        time.sleep(3)