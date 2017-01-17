#Sum List
#Create a program that prints the sum of all the values in the list:
#a = [1, 2, 5, 10, 255, 3]
a = [1,2,5,10,255,3]

def sum_list(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

print "Sum is:",sum_list(a)
