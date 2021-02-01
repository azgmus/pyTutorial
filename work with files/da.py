# file = open('text.txt', 'w')
# file.write('hello')
# file.close()

file = open('oeis.org/A111133/b111133.txt', 'r')
for line in file:

    print(line)
file.close()

class da:
    def __init__(self, das):
        self.das = das


dalist = []
dalist.append(da('da'))
print(dalist[0])
if isinstance(dalist[0],da):
    print('da')