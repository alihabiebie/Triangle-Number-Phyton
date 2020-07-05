
# 1. 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

p=6
for i in range(p):
    for j in range(i):
        print(i, end=(" "))
    print(" ")

# 2.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

p = 6
for i in range(p):
    for j in range(1, i + 1):
        print(j, end=' ')
    print(" ")


# 3.
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

p = 6
for i in range(p):
    for j in range(5, 5-i, -1):
        print(j, end= " ")
    print(" ")


# 4.
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

p=5
for i in range(p):
    for j in range(i, 5):
        print(i+1, end=(" "))
    print(" ")

# 5.
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

p = 5
for i in range(p):
    for j in range(1, 6-i):
        print(j, end= " ")
    print(" ")


# 6.
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4 
# 5

p = 5
for i in range(p):
    for j in range(5, i, -1):
        print(j, end= " ")
    print(" ")