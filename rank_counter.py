def count(rank, parsed_file):
    for line in parsed_file:
        if "/Valkyrie" in line:
            rank["Valkyrie"] += 1
        elif "/Warrior" in line:
            rank["Warrior"] += 1
        elif "/Berserker" in line:
            rank["Berserker"] += 1
        elif "/Slayer" in line:
            rank["Slayer"] += 1
        elif "/Ninja" in line:
            rank["Ninja"] += 1
        elif "/Sorcerer" in line:
            rank["Sorcerer"] += 1
        elif "/Gunner" in line:
            rank["Gunner"] += 1
        elif "/Archer" in line:
            rank["Archer"] += 1
        elif "/Reaper" in line:
            rank["Reaper"] += 1
    return rank



