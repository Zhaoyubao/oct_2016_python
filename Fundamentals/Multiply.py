#Assignment: Multiply
#Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16])
#and returns a list where each value has been multiplied by 5.
a = [2,4,10,16]

def multiply(arr,multi):
    for i in range(len(arr)):
        arr[i] *= multi
    return arr

print multiply(a,5)
