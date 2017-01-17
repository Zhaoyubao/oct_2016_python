#Assignment: Insertion Sort
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

def insertion_sort(list):
    count = 0
    begin_time = datetime.now()
    for i in range (1, len(list)):
        while i > 0 and list[i] < list[i-1]:
            count += 1
            list[i], list[i-1] = list[i-1], list[i]
            i -= 1
    end_time = datetime.now()
    time = end_time - begin_time
    return (list, count, time)

'''
    for i in range(1, len(list)):
        for j in range(i-1, -1, -1):
            count += 1
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
                i -= 1
'''

random_list = generate_list()
print "=" * 90
print
print "Original list:", random_list
sorted_list, count, time = insertion_sort(random_list)
print
print "  Sorted list:", sorted_list
print
print "If-else Statements Counter:", count
print
print "Time Counter: {}s".format(time)
