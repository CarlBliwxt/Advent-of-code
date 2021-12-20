with open('input02.txt', 'r') as f: 
    words = f.read().split()

i = 1
n = 0
horizontal = 0
depth = 0

while i <= len(words):
    if str(words[n]) == "forward" :
        horizontal += int(words[i])
    if str(words[n]) == "down" :
        depth += int(words[i])
    if str(words[n]) == "up" :
        depth -= int(words[i])
    i += 1
    n += 1
print('part 1:', horizontal * depth)