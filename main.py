from file_parser import parse
from rank_counter import count
from page_downloader import download

'''
Scrape https://moongourd.com/ "Class Rankings" stats for Solo Heal for your desired dungeon & boss
Outputs the number of times a class has been found
'''

if __name__ == '__main__':
    # your desired url here
    url = "https://moongourd.com/eu/hiscores?area=3126&boss=1000&class=All%20Classes"
    # the number of ranks to take into account
    target_ranks = 100
    download(url)
    filename = "input.html"
    rank = {"Valkyrie": 0, "Warrior": 0, "Berserker": 0, "Slayer": 0, "Ninja": 0, "Sorcerer": 0, "Gunner": 0, "Archer": 0, "Reaper": 0}
    parsed_file = parse(filename, target_ranks)
    result = count(rank, parsed_file)
    for i in result:
        print(f"Class: {i}, Appeared {rank[i]} times")
