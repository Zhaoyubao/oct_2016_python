#Assignment: Bubble Sort

#Populate a sample list with 100 values (where each value is a random number between 0 to 10000).
#Implement a bubble sort algorithm that returns a new list that's sorted (with smallest number on the left).
#Do this without creating another list.
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
'''
def bubble_sort(list):
    count = 0
    begin_time = datetime.now()
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            count += 1
            if list[j] > list[j+1]:
                list[j+1], list[j] = list[j], list[j+1]
    end_time = datetime.now()
    time = end_time - begin_time
    return (list, count, time)
'''
def bubble_sort(list):
    count = 0
    begin_time = datetime.now()
    length = len(list)
    while length > 1:
        for i in range(length-1):
            count += 1
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        length -= 1
    end_time = datetime.now()
    time = end_time - begin_time
    return (list, count, time)

random_list = generate_list()
print "=" * 90
print
print "Original list:", random_list
sorted_list, count, time = bubble_sort(random_list)
print
print "  Sorted list:", sorted_list
print
print "If-else Statements Counter:", count
print
print "Time Counter: {}s".format(time)
