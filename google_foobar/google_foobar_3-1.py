
def is_correct(staircase):
    for i in range(1, len(staircase)):
        if (staircase[i] >= staircase[i - 1]) or staircase[i] == 0:
            return False
    return True


output_staircases = []


def find_possibilities(staircase):
    s = 0
    if staircase not in output_staircases:
        output_staircases.append(staircase)

    for i in range(-1, -len(staircase) - 1, -1):
        possible_staircase = []

        for j in range(0, i, -1):
            possible_staircase[:] = staircase
            possible_staircase[i] -= 1

            if j == 0:
                possible_staircase.append(1)
            else:
                possible_staircase[j] += 1
            if is_correct(possible_staircase):
                if possible_staircase not in output_staircases:
                    output_staircases.append(possible_staircase[:])
                    #if len(output_staircases) % 100 == 0:
                        #print(len(output_staircases))
                    #print(len(output_staircases))
                    find_possibilities(possible_staircase)


def solution(n):

    staircases = [n - 1, 1]

    find_possibilities(staircases)

    return len(output_staircases)



def do_the_thing(n):
    staircase = [n]
    i = 1
    while staircase[0] - i > i:
        staircase[0] -= i
        staircase.insert(1, i)
        i += 1
    return staircase


pdif = 0
previous = 0
for i in range(3, 40):
    output_staircases = []
    solutioni = solution(i)

    output_staircases = []

    solutioninext = solution(i + 1)

    dif = solutioninext - solutioni
    thinginext = do_the_thing(i+1)
    print(thinginext[0]-thinginext[1],len(do_the_thing(i + 1)), dif - pdif)
    pdif = dif




#def shuffle(staircase):
#    for i in staircase:
#        possible_staircase = staircase[:]
