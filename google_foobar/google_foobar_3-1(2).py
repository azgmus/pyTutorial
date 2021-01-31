def is_correct(staircase):
    for i in range(1, len(staircase)):
        if (staircase[i] >= staircase[i - 1]) or staircase[i] == 0:
            return False
    return True

def do_the_thing(n):
    staircase = [n]
    i = 1
    while staircase[0] - i > i:
        staircase[0] -= i
        staircase.insert(1, i)
        i += 1
    return staircase


def find_possibilities(thinge):

    thing = thinge[:]

    for i in range(thing[0] - thing[1]):
        thing[0] -= 1
        for j in range(1, len(thing)):

            thing[j] += 1
            if is_correct(thing):
                print(thing)
                find_possibilities(thing)
            else:

                thing[j] -= 1

    thing = thinge[:]
    if len(thing) > 2:
        thing[-1] -= 1
        thing[0] += 1
        if thing[-1] == 0:
            thing.pop()

        print(thing)
        find_possibilities(thing)
    if len(thing) == 2:
        thing[1] -= 1
        thing[0] += 1
        if thing[1] > 1:
            find_possibilities(thing)
        print(thing)





thing = do_the_thing(10)
print(thing)
find_possibilities(thing)