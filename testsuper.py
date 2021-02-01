def solution(num):
    F = [0 for i in range(num + 1)]
    F[0] = 1
    F[1] = 1

    for n in range(2, num + 1):
        for k in range(num, n - 1, -1):
            F[k] = F[k] + F[k - n]
    
    return F[num] - 1

print(solution(3))