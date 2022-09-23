# Write a program to print your name.
print('lokesh_bs')

#Write a program for a Single line comment and multi-line comments
# single line comments
# print my name here


'''
multi line comments
print('lokesh_bs') #print my name here
'''

#Define variables for different Data Types int, Boolean, char, float, double and print on the Console
a = 50  # integer
print("data type of a:", type(a))
b = 'Lokesh'  # string
print("data type of b:", type(b))
c = 3.142  # float
print("data type of c:", type(c))
d = 'a'  # Char
print("data type of d:", type(d))


#Define the local and Global variables with the same name and print both variables and
#understand the scope of the variables
'''
here i , j are global variables
and we have access globally
'''
i = 5
j = 6


def sum(i, j):
    '''
      k have block scope and we access global variables in block scope but
      variable declared in block scope is not accessible globally
    '''

    k = i+j
    print(k)


sum(5, 5)
