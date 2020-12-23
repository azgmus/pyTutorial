a = ['da', 'net', 'da', 'da', 'net', 'da']
count = [a.count(i) for i in set(a)]
words = {}

[words.update({a.count(word): word}) for word in a if word not in words]
print(words)
