with open('input_d03.txt', 'r') as file:
    data = file.read().strip()

rucksacks = data.split('\n')

prio_1 = 0
for rs in rucksacks:
    L = len(rs)
    comp1 = rs[:L // 2]
    comp2 = rs[L // 2:]

    for item in comp1:
        if item in comp2:
            value = ord(item) - 96 if item.islower() else ord(item) - 64  + 26
            prio_1 += value
            break

print(f'First task priority: {str(prio_1)}')

x = 0
prio_2 = 0
while x < len(rucksacks):
    bag1 = rucksacks[x]
    bag2 = rucksacks[x + 1]
    bag3 = rucksacks[x + 2]

    for item in bag1:
        if item in bag2 and item in bag3:
            value = ord(item) - 96 if item.islower() else ord(item) - 64 + 26
            prio_2 += value
            x += 3
            break

print(f'First task priority: {str(prio_2)}')