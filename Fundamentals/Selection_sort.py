#Assignment: Selection Sort
from random import randint
from datetime import datetime

def generate_list():
    while 1:
        len = input("Input List Length:")
        if isinstance(len, int) and len > 1:
            break
        else:
            print "Invalid Value!"
            continue
    return [randint(0,10000) for i in range(len)]

def selection_sort(list):
    count = 0
    begin_time = datetime.now()
    for i in range(len(list)-1):
        min_idx = i
        for j in range(i+1, len(list)):
            count += 1
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    end_time = datetime.now()
    time = end_time - begin_time
    return (list,count,time)

random_list = generate_list()
print "=" * 90
print
print "Original list:", random_list
sorted_list, count, time = selection_sort(random_list)
print
print "  Sorted list:", sorted_list
print
print "If-else Statements Counter:", count
print
print "Time Counter: {}s".format(time)
