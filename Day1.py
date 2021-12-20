with open ('input01.txt','r') as f:
    document = f.read()
    array = []
    for n in document.split():
        array.append(int(n)) 
first = array[0]
counter_1 = 0
for i in range(1, len(array)):
    if array[i]> first :
        counter_1 += 1 
    first = array[i]

print('For part 1:',counter_1)

counter_2 = 0 
start = sum(array[0:3])
start_1 = array[0] + array[1] + array[2]
for i in range(1, len(array) - 2):
    lol = array[i] + array[i+1] + array[i+2]
    if lol > start: 
        counter_2 +=1 
    start = lol

print('For part 2: ', counter_2)