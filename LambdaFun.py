def mult(num):
    return lambda x: x*num
obj = mult(4)
print(obj(20))