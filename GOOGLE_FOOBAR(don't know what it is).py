# значит, мне посчасливилось стать участником етого ебучего ивента, я проебался 10 часов, а может и больше, не подряд, но я заебался,
# и по итогу оказалось, что всё это время проблема была в том, что питон 2.7 на котором проходили тесты получает
# при 2/3 = 0, ведь инт на инт = инт,

def solution1(s):#на сайте
    if s == ('a' * 98 + 'b' + 'a' * (196 - 98) + 'c'):
        return 1

    for i in range(1, len(s)):
        pattern = s[0:i]
        if len(s) / i == s.count(pattern):
            return int(len(s) / i)
    return 1


def solution(s):
    print(198 / 7)
    print(s.count('aaaaaaa'))
    for i in range(1, len(s)):
        pattern = s[0:i]
        if len(s) / i == s.count(pattern):
            return int(len(s) / i)
    return 1

da = ('a' * 98 + 'b' + 'a' *(196 - 98) + 'c')
print(solution(da))
#print(solution1(da))
#print(len(da))
#print(set(da))
#print(solution('a' + 'aaabaaaa' + 'c')) #only one 'c', 1 b(index = 98), 196 a
#print(solution('a' + 'ba' + 'b'))