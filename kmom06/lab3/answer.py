#!/usr/bin/env python3

"""
84d613d37d10ac8a7b06a2cf74bc18dd
oopython
lab3
v2
madz21
2024-02-18 17:56:55
v4.0.0 (2019-03-05)

Generated 2024-02-18 18:56:56 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `16` up to `30`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#
def rec_sum(tal):
    """ Recursiv sum """
    sum_=tal
    if tal>16:
        sum_=sum_+rec_sum(tal-1)
    return sum_

#print(rec_sum(30))
ANSWER = rec_sum(30)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that searches for the maximum
# element of a list and returns that number.
# Find the maximum value in the list `[2, 5, 3, 13, 9, 1, 11, 8, 7]`.
#
# Answer with the maximumx value.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1=[2, 5, 3, 13, 9, 1, 11, 8, 7]
def look_max(number):
    """Look for max number """
    if number==1:
        return list1[number-1]
    max_=look_max(number-1)
    #print(max)
    if max_>list1[number-1]:
        return max_
    return list1[number-1]


ANSWER = look_max(8)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `1` in the list `[2, 5, 3, 13, 9, 1, 11, 8, 7]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1=[2, 5, 3, 13, 9, 1, 11, 8, 7]

def find_element2(list_, to_find,index):
    """ Find element in list """
    if not list_:
        return -1
    if list_[0]==to_find:
        return index
    index+=1
    return find_element2(list_[1:],to_find,index)

def find_element(list_, to_find):
    """ Find element in list """
    if not list_:
        return False
    if list_[0]==to_find:
        return True
    return find_element(list_[1:],to_find)

def print_content(list_):
    """ Print content from list """
    if len(list_)==0:
        return
    print(list_[0])
    print_content(list_[1:])

#print(look_index(8,1))
#print_content(list1)
#print(find_element2(list1,20,-1))

ANSWER = find_element2(list1,1,0)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `20` in
# the list `[2, 5, 3, 13, 9, 1, 11, 8, 7]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = find_element2(list1,20,0)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `4` to the
# power of `3`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def power(base,exp):
    """ Calculate the power """
    if exp==1:
        return base
    return base*power(base,exp-1)

ANSWER = power(4,3)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "Frontwards" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#

def backward(word,newword):
    """ Make a word backwards """
    if len(word)==0:
        return newword
    newword=newword+word[len(word)-1]
    return backward(word[:len(word)-1],newword)

ANSWER = backward("Frontwards","")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a recursive function in the code below that calculates the "lowest
# common multiple" between two numbers.
# It should return the smallest positive integer that is divisible by both
# "10" and "5".
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
def lcm(one,two,value):
    """ Least Common Multiplier """
    if value==one*two:
        return value
    if value%one==0 and value%two==0:
        return value
    value+=1
    return lcm(one,two,value)

#print(lcm(10,5,1))

ANSWER = lcm(10,5,1)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)


dbwebb.exit_with_summary()
