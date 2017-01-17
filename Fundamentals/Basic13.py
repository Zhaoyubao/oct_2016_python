#The Basic 13

#Print 1-255
#Print all the integers from 1 to 255.

def print_1to255():
    for num in range(1,256):
        print num

#Print Odds 1-255
# Print all odd integers from 1 to 255.

def print_odds_1to255():
    for odd in range(1,256,2):
        print odd

#Print Ints and Sum 0-255
# Print integers from 0 to 255, and with each integer print the `sum` so far.

def print_ints_sum_0to255():
    sum = 0
    for num in range(256):
        sum += num
        print "Number:{}   Sum:{}".format(num,sum)

#Iterate and Print Array
# Iterate through a given array, printing each value.

def print_array_vals(arr):
    for val in arr:
        print val


#Find and Print Max
# Given an array, find and print its largest element.

def print_max_of_array(arr):
    max = 0
    for num in arr:
        if num > max:
            max = num
    print "Max:{}".format(max)
    # print "Max:",max

#Get and Print Average
#Analyze an array’s values and print the average.

def print_average_of_array(arr):
    sum = 0.0;
    for num in arr:
        sum += num;
    print "Average:{}".format(sum/len(arr))

#Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).

def return_odds_array_1to255():
    arr = []
    for num in range(1,256,2):
        arr.append(num)
    return arr

#Square the Values
# Square each value in a given array, returning that same array with changed values.

def square_arra_vals(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]
    return arr

#Greater than Y
# Given an array and a value `Y`, count and print the number of array values greater than `Y`.

def return_array_count_greater_than_y(arr,y):
    count = 0
    for num in arr:
        if num > y:
            count += 1
    return count

#Zero Out Negative Numbers
# Return the given array after setting any negative values to zero.

def zero_out_array_negative_vals(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr

#Max, Min, Average
# Given an array, print the `max`, `min` and `average` values for that array.

def print_maxminaverage_array_vals(arr):
    max = arr[0]
    min = arr[0]
    sum = 0.0
    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num
        sum += num
    print "Max:{} Min:{} Average:{}".format(max,min,sum/len(arr))

#Shift Array Values
# Given an array, move all values forward by one index, dropping the first and leaving a `0` value at the end.

def shift_array_vals_left(arr):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = 0
    return arr

#Swap String For Array Negative Values
# Given an array of numbers, replace any negative values with the string `'Dojo'`.

def swap_string_for_array_negative_vals(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = "Dojo"
    return arr
