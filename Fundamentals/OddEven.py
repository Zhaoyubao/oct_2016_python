#Assignment: Odd / Even
#Create a function that counts from 1 to 2000. As it loops through each number,
#have your program generate the number and specify whether it's an odd or even number.

def odd_even():
    for num in range(1,2001):
        if num % 2 == 0:
            odd_even = "even"
        else:
            odd_even = "odd"
        print "Number is {}.  This is an {} number.".format(num, odd_even)

odd_even()
