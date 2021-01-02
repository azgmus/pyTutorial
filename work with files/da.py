# file = open('text.txt', 'w')
# file.write('hello')
# file.close()

file = open('text.txt', 'r')
#file.write('hello')
file.close()

class da:
    def __init__(self, das):
        self.das = das


dalist = []
dalist.append(da('da'))
print(dalist[0])
if isinstance(dalist[0],da):
    print('da')