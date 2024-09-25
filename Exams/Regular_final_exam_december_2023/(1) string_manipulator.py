string = input()
while True:
    cmd = input()
    if cmd.startswith("Translate"):
        parts = cmd.split()
        char1, char2 = parts[1], parts[2]
        string = string.replace(char1, char2)
        print(string)
    elif cmd.startswith("Includes"):
        substr = cmd.split()[1]
        print(substr in string)
    elif cmd.startswith("Start"):
        substr = cmd.split()[1]
        print(string.startswith(substr))
    elif cmd.startswith("Lowercase"):
        string = string.lower()
        print(string)
    elif cmd.startswith("FindIndex"):
        char = cmd.split()[1]
        print(string.rfind(char))
    elif cmd.startswith("Remove"):
        parts = cmd.split()
        index, count = int(parts[1]), int(parts[2])
        string = string[:index]+string[index+count:]
        print(string)
    elif cmd.startswith("End"):
        break