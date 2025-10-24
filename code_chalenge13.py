#star
for z in range(1, 4, 1):
    for x in range(1,4,1):
        print(" ", end=" ")
    for y in range(3, z, -1):
        print(" ", end=" ")
    for v in range(1, z, 1):
        print("*", end=" ")
    for w in range(0, z, 1):
        print("*", end=" ")
    print()
for z in range(1, 3, 1):
    for x in range(1,4,1):
        print(" ", end=" ")
    for y in range(0, z, 1):
        print(" ", end=" ")
    for v in range(2, z, -1):
        print("*", end=" ")
    for w in range(3, z, -1):
        print("*", end=" ")
    print()
#pyramids
for z in range(1, 7, 1):
    for x in range(6, z, -1):
        print(" ", end=" ")
    for y in range(1, z, 1):
        print("*", end=" ")
    for v in range(0, z, 1):
        print("*", end=" ")
    print()
for z in range(1, 7, 1):
    for x in range(6, z, -1):
        print(" ", end=" ")
    for y in range(1, z, 1):
        print("*", end=" ")
    for v in range(0, z, 1):
        print("*", end=" ")
    print()
for z in range(1, 7, 1):
    for x in range(6, z, -1):
        print(" ", end=" ")
    for y in range(1, z, 1):
        print("*", end=" ")
    for v in range(0, z, 1):
        print("*", end=" ")
    print()
#trunk
for z in range(5):
    for x in range(4):
        print(" ", end= " ")
    print("*", end= " ")
    print("*", end= " ")
    print("*", end= " ")
    print()
