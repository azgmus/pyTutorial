file = open('b111133.txt', 'r')
answers = dict()
print('{', end='')
for line in file:


    line = line.split()
    answers[int(line[0])] = int(line[1])
    print(line[0], ':', line[1], end=', ')
file.close()
print('}')
print(answers[200])