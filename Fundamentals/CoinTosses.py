#Assignment: Coin Tosses
#You're going to create a program that simulates tossing a coin 5,000 times.
#Your program should display how many times the head/tail appears.
import random

def coin_tosses():
    head = 0
    tail = 0
    coin = ["head","tail"]
    for i in range(1,5001):
        num = round(random.random())
        if num == 1:
            head += 1
            idx = 0
        else:
            tail += 1
            idx = 1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(i, coin[idx], head, tail)
    print "Ending the program, thank you!"

coin_tosses()


def coin_tosses2():
    counter = {
        'head': 0,
        'tail': 0
    }
    for i in range(1, 5001):
        head_tail = random.choice(['head','tail'])
        counter[head_tail] += 1
        print "Attempt #{}: Throwing a coin... It's a {}! ...Got {} head(s) so far and {} tail(s) so far.".format(i, head_tail, counter['head'], counter['tail'])

# coin_tosses2()
