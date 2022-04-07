some_lst = [57.8, 46.51, 97, 55.6, 6, 77.08, 88.8, 106.6, 77.77, 33.5]
print(some_lst)
some_str = ''
for ind, elem in enumerate(sorted(some_lst)):
    some_str += str(int(elem)).zfill(2) + ' руб ' + str(int(elem * 100) % 100).zfill(2) + ' коп, '
print(some_str)
some_str = ''
for ind, elem in enumerate(sorted(some_lst, reverse=True)):       # 5 самых больших чисел
    some_str += str(int(elem)).zfill(2) + ' руб ' + str(int(elem * 100) % 100).zfill(2) + ' коп, '
    if ind == 4:
        break
print(some_str)
