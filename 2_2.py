some_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
some_lst2 = []
for i, e in enumerate(some_lst):
    ind = 0
    while ind < len(e):
        if e[ind].isdigit() == True:
            some_lst2.append('\"')
            break
        ind += 1
    some_lst2.append(e)
    ind = 0
    while ind < len(e):
        if e[ind].isdigit() == True:
            some_lst2.pop()
            some_lst2.append(e)
            some_lst2.append('\"')
           # print(some_lst[i])
            break
        ind += 1

    ind = 0
    while ind < len(e):
        if e[ind].isdigit() == True:
            a = some_lst2.index(e)
            if ind == 0:
                some_lst2[a] = some_lst2[a].zfill(2)
            else:
                some_lst2[a] = some_lst2[a].zfill(3)
            #print(some_lst2[a])
            break
        ind += 1
print(some_lst2)


