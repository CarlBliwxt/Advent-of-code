steps = [step.strip().split(' ') for step 
    in open('input02.txt', 'r').readlines()]
steps = [[change, int(value)] for change, value in steps]

# part 1
horizontal, depth = 0,0
for change, value in steps:
    if change == 'forward':
        horizontal += value
    elif change == 'down':
        depth += value
    else:
        depth -= value
print(horizontal)
print('part 1:', horizontal * depth)