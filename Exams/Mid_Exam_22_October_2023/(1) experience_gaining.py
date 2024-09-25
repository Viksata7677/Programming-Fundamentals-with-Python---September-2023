needed_exp = float(input())
battles = int(input())
total_exp = 0.0
for n in range(1, battles+1):
    exp = float(input())
    if n % 15 == 0:
        exp = exp * 1.05
    elif n % 3 == 0:
        exp = exp * 1.15
    elif n % 5 == 0:
        exp = exp * 0.9
    total_exp += exp
    if total_exp >= needed_exp:
        break
if total_exp >= needed_exp:
    print(f"Player successfully collected his needed experience for {n} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_exp-total_exp:.2f} more needed.")