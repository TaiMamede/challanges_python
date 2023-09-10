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

########################################################
#Another way to write the same code


lista = [(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1)]
print([(i,j,k) for i,j,k in lista if i+j+k !=n])

