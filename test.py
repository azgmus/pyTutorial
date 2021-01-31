def iuelde():
    for i in range(10):
        yield i**2


for da in iuelde():
    print(da)