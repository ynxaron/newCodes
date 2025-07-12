def myNMuliplier(n):
    return lambda a: a * n

befores = range(1, 10)
print(list(map(myNMuliplier(3), befores)))
