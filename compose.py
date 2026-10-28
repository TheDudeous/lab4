def com(funcList, x):
    for f in funcList:
        x = f(x)
    return x


print(com([lambda x: x*2, lambda x: x*3], 2))