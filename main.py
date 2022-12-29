a, b = 1, 2
print('global:', a+b)

def simple_3(a, b):
    print('simple:', a + b)


a, b = 2, 2
print('global:', a+b)
simple_3(a=3, b=4)
