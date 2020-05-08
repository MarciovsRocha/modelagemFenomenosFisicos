def fat(x):
    if (x < 0):
        return -1
    if ((x == 0) or (x == 1)):
        return 1
    else:
        return x*fat(x-1)

print(fat(20))
