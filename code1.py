x = 1
y = 1
z = 1
n = 2
l = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) == n:
                continue
            l.append([i,j,k])
print(l)

