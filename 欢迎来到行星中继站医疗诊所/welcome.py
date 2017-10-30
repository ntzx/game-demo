# coding=utf8

with open('data.txt', 'rb') as f:
    data = f.readlines()
data = [x.decode('utf8').strip() for x in data]

tag2index = {}
paragraphs = []
temp = ''
i = 0
for x in data:
    if not x:
        if temp:
            paragraphs.append(temp)
            i += 1
            temp = ''
    elif x.split('.')[0].__len__() <= 3:
        tag2index[x.split('.')[0]] = i
        temp += x.split('.')[1].strip() + '\n'
    elif x:
        temp += x + '\n'
    else:
        pass
paragraphs.append(temp)
del temp, i, data


def show_para(tag):
    para = paragraphs[tag2index[tag]]
    lines = para.split('\n')

    print('---{}---'.format(tag))
    for i, x in enumerate(lines):
        if x.startswith('link'):
            links = x[5:].split(',')
            a = input(''.join(['->{}\n'.format(t) for t in links]))
            a = a.upper()
            if a in links:
                return a
            elif i < lines.__len__() - 2:
                pass
            else:
                return links[0]
        else:
            print(x)


if __name__ == '__main__':
    tag = 'FIN'
    while True:
        tag = show_para(tag)
