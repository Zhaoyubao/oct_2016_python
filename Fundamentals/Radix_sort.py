# Optional Assignment: Radix Sort
from random import randint
from datetime import datetime

def random_list():
    list = []
    while 1:
        length = input("Input list length:")
        if length > 1:
            r = input("Input random value range:")
            if r > 0:
                break
            print "Invalid Range!"
        else:
            print "Invalid Length!"
    for i in range(length):
        list.append(randint(0,r))
    return list

def get_digit_from_position(num,pos):
    digit = (num / 10**pos) % 10
    return digit

def generate_list(two_dimension_list):
    list =[]
    for row in two_dimension_list:
        for num in row:
            list.append(num)
    return list

def radix_sort(list):
    counter = 0
    max_digit = 0
    for num in list:                       # calculate max digit of number in the list
        if max_digit < len(str(num)):
            max_digit = len(str(num))
    begin_time = datetime.now()
    for i in range(max_digit):
        two_dim_list = [[] for j in range(10)]   # create a two-dimensin list
        for num in list:
            digit = get_digit_from_position(num,i)
            two_dim_list[digit].append(num)
            counter += 1
        list = generate_list(two_dim_list)
    end_time = datetime.now()
    time = end_time - begin_time
    return (list,counter,time)


list = random_list()
print "========================"
print "Original List:",list
print
print "  Sorted List:",radix_sort(list)[0]
print
print "Operations Counter:{}".format(radix_sort(list)[1])
print
print "Time Counter: {}s".format(radix_sort(list)[2])
