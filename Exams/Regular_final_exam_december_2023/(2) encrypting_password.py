
# 80/100
def is_valid(password):
    groups = form_groups(password)
    if groups is None:
        return False
    return (one_char(groups[0]) and groups[0] == groups[-1] and
            groups[1].isdigit() and groups[2].islower() and groups[3].isupper() and
            "<" not in groups[4] and ">" not in groups[4])


def form_groups(password):
    if ">" not in password:
        return None
    first_group, rest = password.split(">", 1)
    if "<" not in rest:
        return None
    rest, last_group = rest.split("<", 1)
    split = rest.split("|")
    if len(split) != 4:
        return None
    return [first_group] + split + [last_group]


def encrypt(password):
    middle_groups = form_groups(password)[1:-1]
    return "".join(middle_groups)


def one_char(string):
    if not string:
        return False
    ch1 = string[0]
    for ch2 in string:
        if ch1 != ch2:
            return False
    return True


N = int(input())
for k in range(N):
    password = input()
    if is_valid(password):
        print(f"Password: {encrypt(password)}")
    else:
        print("Try another password!")