
#Write a function for arithmetic operators(+,-,*,/)
def arthimatic_operator(a, b):
    print("Additon +::", a+b)
    print("Subtraction -::", a-b)
    print("Multiplication *::", a*b)
    print("Division /::", a/b)


arthimatic_operator(5, 5)


#Write a method for increment and decrement operators(++, --)
#in python there is no icremenet operator as in other languages we can acheive.this operator by for in range method
def incremetn():
    for i in range(1,10):
        print(i)


incremetn()

def decrement():
    for i in range(10, 0, -1):
        print(i)

decrement()  


#Write a program to find the two numbers equal or not.

def eql_or_not(a,b):
    if(a==b):
        print('a equals to b')
    else:
        print('a not equals to b')    

eql_or_not(5,2)


#Program for relational operators (<,<==, >, >==)

def greater_or_equal(a,b):
    if a>=b:
        print('a greater_or_equlas to b')
    else:
        print('a lesser_or_equlas to b')    

greater_or_equal(5,5)


#Print the smaller and larger number

#using the python in bulit methods
def smaller_larger(a,b):
    print(min(a,b),'smaller number');
    print(max(a,b),'larger number');

smaller_larger(5,1);


#using comaparison
def smallerLarger(a,b):
    if a>b:
        print('smallernumber',b);
    else:
        print('larger number',a);

smallerLarger(5,1)