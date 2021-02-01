
def is_correct(staircase):
    for i in range(1, len(staircase)):
        if (staircase[i] >= staircase[i - 1]) or staircase[i] == 0:
            return False
    return True


output_staircases = []


def find_possibilities(staircase):

    if staircase not in output_staircases:
        output_staircases.append(staircase[:])
        print(len(output_staircases))
    else:
        return
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
                if possible_staircase[:] not in output_staircases:

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

#print(solution(200), end=', ')
i = 0
while True:
    print(i)
    i+=1





#def shuffle(staircase):
#    for i in staircase:
#        possible_staircase = staircase[:]
