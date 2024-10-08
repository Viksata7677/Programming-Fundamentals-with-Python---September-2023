numbers = list(map(int, input().split(' ')))
time_left_needed = 0
time_right_needed = 0
finish_line = len(numbers) // 2 + 1
left_racer = numbers[:finish_line - 1]
right_racer = numbers[finish_line:][::-1]

for first_racer_time in left_racer:
    time_left_needed += first_racer_time
    if first_racer_time == 0:
        time_left_needed *= 0.80

for second_racer_time in right_racer:
    time_right_needed += second_racer_time
    if second_racer_time == 0:
        time_right_needed *= 0.80

if time_left_needed < time_right_needed:
    print(f"The winner is left with total time: {time_left_needed:.1f}")
else:
    print(f"The winner is right with total time: {time_right_needed:.1f}")