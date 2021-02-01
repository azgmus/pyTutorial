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


def find_possibilities_with_this_len(instaircase, first=False):
    staircase = instaircase[:]

    if staircase[-1] != 1 and first:
        staircase[0] += staircase[-1] - 1
        staircase[-1] = 1
    for i in range(staircase[0] - staircase[1]):
        staircase[i] -= 1
        for j in range(1, len(staircase)):
            staircase[j] += 1
            if is_correct(staircase):
                find_possibilities_with_this_len(staircase)
                staircase[j] -= 1
            else:
                break






def find_possibilities(start_staircase, just_changed=False):
    staircase = start_staircase[:]

    for i in range(staircase[0] - staircase[1]):
        staircase[0] -= 1
        for j in range(i + 1, len(staircase)):
            staircase[j] += 1
            if is_correct(staircase):
                print(staircase)
                find_possibilities(staircase)
                staircase[j] -= 1
            else:

                break



    if len(staircase) > 2:
        if staircase[-1] == 1:
            staircase[0] += staircase.pop()
            find_possibilities(staircase, True)









thing = do_the_thing(20)
print(thing)
find_possibilities_with_this_len(thing)
#find_possibilities(thing)