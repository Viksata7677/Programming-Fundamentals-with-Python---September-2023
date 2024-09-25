shelf = input().split("&")

while True:
    cmd = input()
    if cmd == "Done":
        break
    cmd, rest = cmd.split(" | ", 1)
    if cmd == "Add Book":
        book = rest
        if book not in shelf:
            shelf.insert(0, book)
    elif cmd == "Take Book":
        book = rest
        if book in shelf:
            shelf.remove(book)
    elif cmd == "Swap Books":
        book1, book2 = rest.split(" | ")
        if book1 in shelf and book2 in shelf:
            index1 = shelf.index(book1)
            index2 = shelf.index(book2)
            shelf[index1] = book2
            shelf[index2] = book1
    elif cmd == "Insert Book":
        book = rest
        if book not in shelf:
            shelf.append(book)
    elif cmd == "Check Book":
        index = int(rest)
        if 0 <= index < len(shelf):
            print(shelf[index])

print(", ".join(shelf))
