#Completed November 24th, 2020
#Last Edited November 29th, 2020
#Author: Nicholai Ponomarev
#Student #101182048

#Part A: Software Experiments___________________________________________________
"""
ECOR 1041 Lab 6 Solution Template

Author and Student Number: Nicholai Ponomarev (#101182048)

This file is to be used in conjunction with the detailed lab description for Lab 6
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: Single or Double Quotes - Does it matter?

Example, "haven't" or '"Spam, spam, spam," he said.'

>>> type('Hello')
# Type what you see: <class 'str'>

>>> type("goodbye")
# Type what you see: <class 'str'>

>>> 'Hello'
# Type what you see: 'Hello'

>>> ""     (An empty string - type two quotes with no spaces between them.)
# Type what you see:''

>>> '"Spam, spam, spam," he said.'
# Type what you see: '"Spam, spam, spam," he said.'

>>> "I haven't a clue" 
# Type what you see: "I haven't a clue"

>>> 'I haven't a clue' 
# Type what you see: builtins.IndentationError

Concluding Questions: Generally, either double or single quotes works well but can you give a scenario where one is better than the other?
Double quote are usually use to write a str message or something of the sort while single quotes are usually used to right
a symbol such as 'English' or 'Addition'. It is also more beneficial to use double quotes when writing a print statement with a 
word that contain an apostraphe such as don't, an example would be: print("Don't do this !").
==================

Exercise 2: What operations are permitted with values of type str?

When used with strings, + is the concatenation operator. 

>>> 'Hello, ' + 'world!'
# Type what you see: 'Hello, world!'

When used with strings, * is the replication operator.

>>> "Spam" * 3
# Type what you see: 'SpamSpamSpam'

>>> 3 * "Spam"
# Type what you see:'SpamSpamSpam' (The order of operators does not matter).

>>> "Spam" * 0
# Type what you see: ''

>>> "Spam" * -3
# Type what you see: ''

There are other operators to try now: - and /

>>> "Hello" - "He"
# Type what you see: builtins.TypeError

>>> 'Spam' / 3
# Type what you see: builtins.TypeError


Concluding Questions: What operators work with strings?  Does the order of operands matter?
According to the above results, the operators "+" and "*" work with strings and the order of operators does not matter.
=======================

Exercise 3 : Understand the string representation

Is  the string '123' the same as the integer 123? 

>>> '123' + 456
# Type what you see: builtins.TypeError

>>> '123' + '456'
# Type what you see: '123456'

Concluding Question: When a string looks like a number, is it a number or a string?
When a string looks like a number, it is still a string no matter what unless there is a function within the code causing the 
compiler to interpret the string as a number.
=========
Last edited: November 29th, 2020
"""

#Part B: Designing Function that Process Text___________________________________
#Exercise 4:
def repeat(s: str, n: int) -> str:
 """
 Return s repeated n times; if n is negative, return the
  empty string.
  >>> repeat('yes', 4)
  'yesyesyesyes'
  >>> repeat('no', 0)
  ''
  >>> repeat('no', -2)
  ''
  >>> repeat('yesnomaybe', 3)
  'yesnomaybeyesnomaybeyesnomaybe' 
 """
 return (s*n)

#Excercise 5:
def total_length(s1: str, s2: str) -> int:
 """ 
 Return the sum of the lengths of s1 and s2.
 >>> total_length('yes', 'no')
 5
 >>> total_length('yes', '')
 3
 >>> total_length('YES!!!!', 'Noooooo')
 14
 """
 return len(s1) + len(s2)

#Excercise 6:
def replicate(s1: str) -> str:
 """
 Return the string replicated the same amount
 of times as the lenght of the string.
 >>>replicate('two')
 'twotwotwo'
 >>>replicate('abcd')
 'abcdabcdabcdabcd'
 >>>replicate('a')
 'a'
 """
 return s1*len(s1)

#Main Script:

#Excercise 4:
repeated_string = repeat('yes', 4)
print("The repeated string:", repeated_string)
repeated_string = repeat('no', 0)
print("The repeated string:", repeated_string)
repeated_string = repeat('yesnomaybe', 3)
print("The repeated string:", repeated_string)
repeated_string = repeat('no', -2)
print("The repeated string:", repeated_string)

#Excercise 5:
sum_length = total_length('yes', 'no')
print("The sum of the length of the strings is:",sum_length)
sum_length = total_length('yes', '')
print("The sum of the length of the strings is:",sum_length)
sum_length = total_length('YES!!!!', 'Noooooo')
print("The sum of the length of the strings is:",sum_length)

#Excercise 6:
replicated_string = replicate('two')
print("The replicated string is:", replicated_string)
replicated_string = replicate('abcd')
print("The replicated string is:", replicated_string)
replicated_string = replicate('a')
print("The replicated string is:", replicated_string)
