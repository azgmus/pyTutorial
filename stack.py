favs = []
while True:
    data = input()
    if str.lower(data) == 'q':
        break
    if str.lower(data) == 'r':
        if favs:
            print(favs.pop(), 'removed')
            continue

        else:
            print('no favs to pop')
            continue
    favs.append(data)
