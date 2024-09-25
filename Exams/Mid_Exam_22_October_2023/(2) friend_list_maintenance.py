friends = input().split(", ")

while True:
    cmd = input()
    if cmd == "Report":
        break
    cmd, rest = cmd.split(" ", 1)
    if cmd == "Blacklist":
        name = rest
        index = None
        for i in range(len(friends)):
            if friends[i] == name:
                index = i
                break
        if index is not None:
            friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif cmd == "Error":
        index = int(rest)
        if 0 <= index < len(friends):
            name = friends[index]
            if name != "Lost" and name != "Blacklisted":
                friends[index] = "Lost"
                print(f"{name} was lost due to an error.")
    elif cmd == "Change":
        index, new_name = rest.split(" ", 1)
        index = int(index)
        if 0 <= index < len(friends):
            current_name = friends[index]
            friends[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

blacklisted = 0
lost = 0
for friend in friends:
    if friend == "Blacklisted":
        blacklisted += 1
    elif friend == "Lost":
        lost += 1

print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(" ".join(friends))
