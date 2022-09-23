
# Write a function to add integer values of an array
import re
from unittest import result


def sum_array():
    a = [18, 2, 3, 4, 5]
    total = 0
    for i in range(0, len(a)-1):
        total += a[i]
    print("sum of array:", total)
    print('\n')


sum_array()

# Write a function to calculate the average value of an array of integers


def average_array():
    a = [18, 2, 3, 4, 5]
    average = 0
    total = 0
    for i in range(0, len(a)-1):
        total += a[i]
        average = total/len(a)
    print("average of array:", average)
    print('\n')


average_array()

# Write a program to find the index of an array element


def find_index_of_array(ele):
    a = [18, 2, 3, 4, 5]
    index = -1
    for i in range(0, len(a)-1):
        if (ele == a[i]):
            index = i
            break
    print("index of array:", index)
    print('\n')


find_index_of_array(2)

# Write a function to test if array contains a specific value


def test_array_contains_value(ele):
    a = [18, 2, 3, 4, 5, 6, 7, 8]
    test = False
    for i in range(0, len(a)-1):
        if (ele == a[i]):
            test = True
            break
        else:
            test = False

    if test:
        print('array contains given value')
    else:
        print('array does not contain given value')
    print('\n')


test_array_contains_value(6)

# Write a function to remove a specific element from an array


def remove_element(ele):
    a = [18, 2, 3, 4, 5, 6, 7]
    print(a)
    for i in range(0, len(a)-1):
        if (ele == a[i]):
            a.pop(i)
    print(a)
    print('\n')


remove_element(18)


# Write a function to copy an array to another array
def copy_an_array():
    a = [18, 2, 3, 4, 5]
    b = []
    for i in range(0, len(a)):
        b.append(a[i])
    print(b, 'copied array')
    print('\n')


copy_an_array()

# Write a function to insert an element at a specific position in the array


def insert_an_element(ele, position):
    a = [18, 2, 3, 4, 5, 6, 7]
    a.insert(position, ele)
    print(a, 'inserted element')
    print('\n')


insert_an_element(20, 0)


# Write a function to find the minimum and maximum value of an array
def min_max_of_arary():
    a = [18, 2, 100, 3, 4, 1, 5, 98, .2]
    max = a[0]
    min = a[0]
    for i in range(len(a)-1):
        if (a[i] >= a[i+1]):
            temp_max = a[i]
            temp_min = a[i+1]
            if (temp_max > max):
                max = temp_max
            elif (temp_min < min):
                min = temp_min
        else:
            temp_max = a[i+1]
            temp_min = a[i]
            if (temp_max > max):
                max = temp_max
            elif (temp_min < min):
                min = temp_min

    print(max, "Maximum")
    print(min, "Minimum")
    print('\n')


min_max_of_arary()


# Write a function to reverse an array of integer values
def reverse_array():
    a = [1, 3, 6, 6, 4, 2, 5, ]
    b = []
    b = a[::-1]
    print(a, 'normal array')
    print(b, 'reversed array')
    print('\n')


reverse_array()

# Write a function to find the duplicate values of an array


def duplicate_array():
    a = [1, 5, 4, 6, 8, 6, 3, 5, 5, 1, 3, 19, 1]
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if (a[i] == a[j]):
                print(a[j])
    print('\n')


duplicate_array()

# Write a program to find the common values between two arrays


def common_array():
    a = [1, 2, 3, 4, 5, ]
    b = [10, 3, 5, 8, 7, 46, 1, 3, 1, 3]
    commonEle = []
    # return[element for element in a  if element in b ]
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] == b[j]):
                commonEle.append(a[i])
    print(commonEle)
    print('\n')


print(common_array())


# Write a method to remove duplicate elements from an array
def delete_commonEle():
    a = [1, 5, 4, 6, 8, 6, 3, 5, 5, 1, 3, 19, 1]
    a = list(set(a))
    print(a)
    print('\n')


delete_commonEle()

# Write a method to find the second largest number in an array


def second_largest_number_in_array():
    a = [18, 2, 100, 3, 4, 1, 5, 98, 122,6565]
    max = a[0]
    second_largest_number = a[0]
    for i in range(len(a)-1):
        if (a[i] >= a[i+1]):
            temp_max = a[i]
            second_largest_number=max
            if (temp_max > max):
                max = temp_max
            
        else:
            temp_max = a[i+1]
            second_largest_number=max
            if (temp_max > max):
                max = temp_max
           
    print(second_largest_number, "second_largest_number")
    print('\n')

second_largest_number_in_array()

# Write a method to find number of even number and odd numbers in an array
def find_even_number_in_array():
    a=[1,2,3,4,5,6,8]
    for i in range(len(a)-1):
        if(a[i]%2==0):
            print(a[i],'even number')
        else:
            print(a[i],'odd number')    

    print('\n')
find_even_number_in_array()            

# Write a function to get the difference of largest and smallest value
def get_difference_of_largest_and_smallest_value():
    a = [18, 2, 100, 3, 4, 1, 5, 98, 99]
    max = a[0]
    min = a[0]
    difference=0
    for i in range(len(a)-1):
        if (a[i] >= a[i+1]):
            temp_max = a[i]
            temp_min = a[i+1]
            if (temp_max > max):
                max = temp_max
            elif (temp_min < min):
                min = temp_min
        else:
            temp_max = a[i+1]
            temp_min = a[i]
            if (temp_max > max):
                max = temp_max
            elif (temp_min < min):
                min = temp_min
    print(max,min)            
    difference=max-min
    print(difference)
    print('\n')
get_difference_of_largest_and_smallest_value()   


#. Write a method to verify if the array contains two specified elements(12,23)
def array_contains_two_element():
    a = [18, 2, 100, 3, 4, 1, 5, 98, 99,12,23];
    result=[12,23]
    verify=False;
    verify=all(x in a for x in result)
    print(verify)
    print('\n')
array_contains_two_element()

#Write a program to remove the duplicate elements and return the new array
def remove_duplicates():
    a = [18, 2, 100, 3, 4, 1, 5, 98, 99,12,23];
    a = list(set(a))
    return a;

print(remove_duplicates())               