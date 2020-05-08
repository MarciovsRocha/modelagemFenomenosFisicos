def fat(x):
    if (x < 0):
        return -1
    if ((x == 0) or (x == 1)):
        return 1
    else:
        return x*fat(x-1) 

q1_1 = [1/n for n in range(1,10)]
q1_2 = [1/n for n in range(1,11,+2)]
q1_3 = [fat(n) for n in range(1,10)]
q1_4 = [(1/(2**n)) for n in range(0,10)]
