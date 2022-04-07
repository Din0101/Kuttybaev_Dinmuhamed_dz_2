some_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i = 0
while i < len(some_lst):
    some_lst[i] = some_lst[i].lower()
    b = some_lst[i].rindex(" ")
    n = 0
    some_word = ''
    while n < len(some_lst[i]):
        if n == b+1:
            some_word += some_lst[i][b+1].upper()
        else:
            some_word += some_lst[i][n]
        n += 1
    some_lst[i] = some_word
    i += 1
print(some_lst)
for ind, elem in enumerate(some_lst):
    print('Hello, {}!'.format(elem.split()[-1]))

