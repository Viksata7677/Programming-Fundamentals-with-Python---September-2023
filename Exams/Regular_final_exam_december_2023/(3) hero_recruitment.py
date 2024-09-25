heroes = {}
while True:
    cmd = input().split()
    if cmd[0] == "Enroll":
        hero = cmd[1]
        if hero in heroes:
            print(f"{hero} is already enrolled.")
        else:
            heroes[hero] = []
    elif cmd[0] == "Learn":
        hero, spell = cmd[1], cmd[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        elif spell in heroes[hero]:
            print(f"{hero} has already learnt {spell}.")
        else:
            heroes[hero].append(spell)
    elif cmd[0] == "Unlearn":
        hero, spell = cmd[1], cmd[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
        elif spell not in heroes[hero]:
            print(f"{hero} doesn't know {spell}.")
        else:
            heroes[hero].remove(spell)
    elif cmd[0] == "End":
        break

print("Heroes:")
for hero in heroes:
    spells = heroes[hero]
    print(f"== {hero}: {', '.join(spells)}")