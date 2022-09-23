import re
# Different ways creating a string
string1 = 'LokeshBs'
string2 = "lokesh_bs"
string3 = '5454'
string4 = 'lokeshbs@gmail.com'

# Concatenating two strings using + operator
fname = 'Lokesh'
lname = 'bs'
full_name = fname+lname
print(full_name)

# Finding the length of the string
lenght = len(fname)
print(lenght)
print('\n')

# Extract a string using Substring
spce_full_name = full_name[0:6]
print(spce_full_name)
print('\n')

# Searching in strings using index()
str1 = fname.index('h')
print(str1)
print('\n')

# Matching a String Against a Regular Expression With matches()
regex = r'([\w\.-]+)@([\w\.-]+)'
mailId = ('hello lokeshbs0608@gmail.com')
matches = re.findall(regex, mailId)
for tuple in matches:
    print("Username: ", tuple[0])  # username
    print("Host: ", tuple[1])  # host
    print('\n')


# Comparing strings
fname = 'lokeshbs0608@gmail.com'
lname = 'hello lokeshbs0608'
if (fname == lname):
    print('string matches')
else:
    print('string not matches')
print('\n')    



#startsWith(), endsWith() and compareTo()
text='Python is easy to understand'
result=text.startswith('Pyhton')
print(result)
print('\n')  
result=text.endswith('Pyhton')
print(result)
print('\n')  



#Trimming strings with strip()
stripeString='   lokeshbs   '
print(stripeString.strip()) #returns a new string after removing any leading and trailing whitespaces including tabs 
print('\n')
print(stripeString.rstrip()) #returns a new string with trailing whitespace removed. 
print('\n')
print(stripeString.lstrip()) #rreturns a new string with leading whitespace removed,
print('\n')


# Replacing characters in strings with replace()
stripeString='nanu'
print(stripeString.replace('nanu','sasya')) 
print('\n')


#Splitting strings with split()

spiltString="we are in search of job"
print(spiltString.split())
print('\n')
spiltString1="we#are#in#search#of#job"
print(spiltString.split("#"))
print('\n')
spiltString="we are in ,search of job"
print(spiltString.split(', '))
print('\n')


# Converting integer objects to Strings

dob=456456456456 # integer value
print( type(dob)) #printing type
dob_String=(str(dob)) #converting integer to string
print( type(dob_String)) 
print( dob_String   ) 
print('\n')

# Converting to uppercase and lowercase
fname='LOKESH BS '
upper=fname.lower() #converting upperCase to lowerCase
print(upper)
print('\n')
lower=upper.upper()
print(lower )
print('\n')