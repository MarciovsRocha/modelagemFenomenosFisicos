def myFunc(a,b):
    if ((type(a) == str) and (type(b) == str)):
        return a+b
    elif ((type(a) == int) and (type(b) == int)):
          return a+b
u = 'Hello'
o = 'World'
print(myFunc(u,o))
u = 10
o = 1
print(myFunc(u,o))
