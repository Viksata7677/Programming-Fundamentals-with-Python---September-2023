n = int(input())
magic_word = input()

strings = []

for i in range(n):
    string = input()
    strings.append(string)

print(strings)

filtered_strings = []

for current_string in strings:
    if magic_word in current_string:
        filtered_strings.append(current_string)

print(filtered_strings)
