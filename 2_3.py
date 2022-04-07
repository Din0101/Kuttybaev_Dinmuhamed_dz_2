some_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#print(len(some_lst))
i = 0
l = len(some_lst)
b = 0
while i < l:
    r = 0
    while r < len(some_lst[i]):
        if some_lst[i][r].isdigit() == True:
            if r == 0:
                some_lst[i] = some_lst[i].zfill(2)
            else:
                some_lst[i] = some_lst[i].zfill(3)
            some_lst.insert(i+1, "\"")
            some_lst.insert(i, "\"")
            b += 1
            l += 2
            i += 1
            #print(some_lst[i])
            break
        r += 1
    i += 1
print(some_lst)
#print(b)