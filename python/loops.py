# Write a program to print “Bright IT Career” ten times using for loop
from curses import flash
from ssl import OP_ALL


def bright_it_career():
    for i in range(0, 10):
        print('Bright IT Career')
    print('\n')


bright_it_career()


# Write a python program to print 1 to 20 numbers using the while loop.

def while_loop():
    a = 1
    while (a <= 20):
        print(a)
        a += 1
    print('\n')


while_loop()

# Program to equal operator and not equal operators


def notEqual_or_equal(a, b):
    if a != b:
        print('a not equals b')
    else:
        print('a equlas to b')
    print('\n')


notEqual_or_equal(5, 8)


# Write a program to print the odd and even numbers.
def odd_and_even_numbers(a):
    if a % 2 == 0:
        print('even number', a)
    else:
        print('odd number', a)
    print('\n')


odd_and_even_numbers(5)

# Write a program to print largest number among three numbers.


def largest_among_three_numbers(a, b, c):
    if (a > b) & (a > c):
        print(a, 'largest_among_three_numbers')
    elif (b > a) & (b > c):
        print(b, 'largest_among_three_numbers')
    else:
        print(c, 'largest_among_three_numbers')
    print('\n')


largest_among_three_numbers(7, 2, 3)


# Write a program to print even number between 10 and 20 using while

def while_loop():
    print("WHILE LOOP")
    a = 10
    while (a <= 20):
        if (a % 2 == 0):
            print(a,)
        a = a+1
    print('\n')


while_loop()


# Write a program to print 1 to 10 using the do-while loop statement.

def do_while_loop():
    print('DO WHILE LOOP')
    i = 1
    while True:
        print(i)
        i += 1
        if (i > 10):
            break
    print('\n')


do_while_loop()

# Write a program to find Armstrong number or not


def armStrongNumber(number):

    total = 0
    order = len(str(number))
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit**order
        temp //= 10
    if number == total:
        print(number, 'is a armStrongNumber')
    else:
        print(number, 'is not a armStrongNumber')
    print('\n')


armStrongNumber(1634)


# Write a program to find the prime or not.
flag = False


def primeNumber(a):
    if a > 1:
        for i in range(2, a):
            if (a % i) == 0:
                print(a, 'is not a primeNumber')
                break
            else:
                print(a, 'is  a primeNumber')
                break
    print('\n')

primeNumber(6)


# Write a program to palindrome or not.
def palidrome():
    pali = 'KANAK'
    pali1 = pali[::-1]
    if (pali == pali1):
        print('given string', pali, 'is a palindrome')
    else:
        print('given string', pali, 'is a  not palindrome')
    print('\n')

palidrome()

# Program to check whether a number is EVEN or ODD using switch


def switch_odd_even(a):
    b = a % 2 == 0
    if(b):
        print(a, 'is a even number')
    else:
        print(a, 'is a odd number')    
    print('\n')

switch_odd_even(6)

#Print gender (Male/Female) program according to given M/F using switch
def switch_F_M(a):
    if('F'):
        print('Female')
    else:
        print('Male')    
    print('\n')

switch_F_M('M')