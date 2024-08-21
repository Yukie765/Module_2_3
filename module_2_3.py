my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0
list_end = len(my_list)
while i != list_end:
    if my_list[i] > 0:
        print(my_list[i])
        i = i + 1
        continue
    elif my_list[i] < 0:
        break
    i = i + 1
