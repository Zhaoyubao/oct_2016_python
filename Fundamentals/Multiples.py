#Multiples

#Part I
#Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use array to do this exercise.
def print_odds():
    for num in range(1,1001,2):
        print num

def print_odds2():
    for num in range(1,1001):
        if num % 2 != 0:
            print num
print_odds2()

#Part II
#Create another program that prints all the multiples of 5 from 5 to 1,000,000.
def print_mults():
    i = 5
    while i < 1000001:
        print i
        i +=5

def print_mults2():
    for i in range(5,1000001,5):
        print i

# print_mults()
