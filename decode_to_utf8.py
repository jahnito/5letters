vocabulary = 'russian.txt'
voc_utf8 = 'russsian.utf8.txt'

with open(vocabulary, encoding='cp1251') as v:
    data = v.read()
    with open(voc_utf8, 'w') as go:
        go.write(data)
