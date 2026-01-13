import random

class Team:
    def __init__(self, name, country, place):
        self.name = name
        self.country = country
        self.place = int(place)


teams = []

print("Enter 16 teams:")
for i in range(16):
    name, country, place = input().split()
    teams.append(Team(name, country, place))


first = []
second = []

for t in teams:
    if t.place == 1:
        first.append(t)
    else:
        second.append(t)

random.shuffle(first)
random.shuffle(second)

matches = []

for t1 in first:
    possible = []

    for t2 in second:
        if t1.country != t2.country:
            if not (t1.country == "Ukraine" and t2.country == "Russia"):
                if not (t1.country == "Russia" and t2.country == "Ukraine"):
                    possible.append(t2)

    opponent = random.choice(possible)
    matches.append((t1, opponent))
    second.remove(opponent)

print("\nMatches:")
for m in matches:
    print(m[0].name, "vs", m[1].name)