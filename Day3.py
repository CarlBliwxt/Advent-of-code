import numpy as np
# 
with open ('input03.txt','r') as f:
    text = f.read().split()
y = 0
v = np.zeros(len(text)*12)
n = 0
for x in range(len(text)):
    num_str = str(text[x])
    y = 0 
    while y < 12 : 
        digit = num_str[y:y+1]
        v[n] = digit
        y += 1
        n += 1
i = 0
B = np.zeros(12)
gamma_array= []
epsilion_array = []
for x in range(0,12):
    i = x
    lol = 12
    A = 0
    while i < (len(text) * 12) - lol:
        A += v[i] 
        i += 12
    B[x] = A
    lol -= 1
    if B[x] > 500: 
        gamma_array.append("1")
        epsilion_array.append("0")
    else:
        gamma_array.append("0")
        epsilion_array.append("1")
x = ("".join(gamma_array))
y = ("".join(epsilion_array))
gamma = int(x,2)
epsilion = int(y,2)
print(gamma * epsilion)

