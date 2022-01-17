#Completed December 8th, 2020
#Last Edited December 11th, 2020
#Author: Nicholai Ponomarev
#Student #101182048

#Exercise 1:
"""
Step 1: Try this experiment in the Python Shell.
>>> point1 = [1.0, 2.0]
>>> point1
What is displayed when Python evaluates point1?
Answer: [1.0, 2.0]

Step 2: What is displayed when Python evaluates point1?
>>> point1.append(3.0)
>>> point1
Answer: [2.0, 3.0, 3.0]
What is displayed each time Python evaluates point1?
>>> point1.pop(0)
>>> point1

>>> point1.pop()
>>> point1
Answer: []

Step 3: What is displayed when the last two statement are evaluated?
>>> point1 = (1.0, 2.0)
>>> type(point1)
>>> point1
Answer: (1.0, 2.0)

Step 4: What is displayed when Python evaluated x and y?
>>> x = point1[0]
>>> y = point1[1]
>>> x 
>>> y 
Answer: 1.0
        2.0
        
What is displayed when Python evaluates x and y?
>>> point2 = (4.0, 6.0)
>>> x, y = point2
>>> x
>>> y
Answer: 4.0
        6.0
        
Step 5: What is displayed when Python exceutes each statement?
>>> point2[0] = 2.0 # Can we change the point to (2.0, 6.0)?
Answer: builtins.TypeError: 'tuple' object does not support item assignment
>>> point2.append(4.0) # Can we add a third coordinate?
Answer: builtins.AttributeError: 'tuple' object has no attribute 'append'
>>> point2.pop(0) # Can we remove the first coordinate?
Answer: builtins.AttributeError: 'tuple' object has no attribute 'pop'

Step 6: Try this experiment, which demonsrates how to create a list of tuples
that represen the points (1.0, 5.0), (2.0, 8.0) and (3.5, 12.5).
>>> points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]
>>> points[0]
>>> points[1]
>>> points[2]
Answer: (1.0, 5.0)
        (2.0, 8.0)
        (3.5, 12.5)
"""

#Test Function:
def test_int(testingMessage: str, actualResult: int, expectedResult: int) -> int:
 """
 This function is designed to shorten the amount of code written.
 Instead off all the different tests done, this function will return 
 a value of 1 if the test is passed or a value of 0 if the test is 
 failed.
 """
 print(testingMessage)
 print("Expected result:",expectedResult,"Actual result:", actualResult)
 
 if actualResult == expectedResult:
  print("Test Passed!")
  global passCount      #Global must be used so that the variable can be accessed from outside the function.
  passCount += 1        #camelCase variable = Personal Preference.
  return 1
 
 elif actualResult != expectedResult:
  print("Test Failed!")
  global failCount      #Global must be used so that the variable can be accessed from outside the function.
  failCount += 1        #camelCase variable = Personal Preference.
  return 0

#Exercise 2 Function Definition:
def average(list1: list) -> list:
 """
 The function takes a list of tuples, with each tuple containing
 3 non-negative integers. The function returns a new list of tuples
 containing the average values of the numbers in the tuple at the same 
 position in the original list.
 >>>average([(27, 219, 134), (0, 0, 0), (1, 2, 30)])
 [(126, 126, 126), (0, 0, 0), (11, 11, 11)]
 >>>average([(1, 5, 9), (0, 3, 0), (1, 10, 97)])
 [(5, 5, 5), (1, 1, 1), (36, 36, 36)]
 """
 
 SUMtuple = 0
 lengthList = len(list1)
 
 if lengthList == 0:
  return []
 
 for element in range(lengthList):
     for b in list1[element]:
         SUMtuple += b
     average = (SUMtuple // 3) #can also do "average = int(SUMtuple/3)" to convert any floating point values to integer values.
     list1 [element] = (average, average, average)
     SUMtuple = 0
 return list1

#Exercise 3:
"""
Step 1: What is displayed when points is evaluated?
>>> points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}
>>> points
Answer: {(10.0, -2.0), (1.0, 2.0), (4.0, 6.0)}
What is displayed when points is evaluated?
>>> point1 = (1.0, 2.0)
>>> point2 = (4.0, 6.0)
>>> point3 = (10.0, -2.0)
>>> points = {point1, point2, point3}
>>> points
Answer: {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}
What is displayed when points is evaluated?
>>> points = set()
>>> points.add(point1)
>>> points.add(point2)
>>> points.add(point3)
>>> points
Answer: {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}

Step 2: What happens if we try to insert a point that is already in the set?
How many copies of point (4.0, 6.0) are in the set?
>>> points.add(point2)
>>> points
Answer: {(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}
Answer: There is still 1 copy in the set of (4.0, 6.0).

Step 3: What is displayed when points[0] is evaluated?
>>> points[0]
Answer: builtins.TypeError: 'set' object is not subscriptable
Answer: Individual points cannot be retrieved from a set because
sets do not have any particular order.

Step 4: What is displayed when this loop is executed?
>>> for point in points:
... print(point)
...
Answer: (4.0, 6.0)
        (4.0, 6.0)
        (10.0, -2.0)
        (4.0, 6.0)
"""
#Exercise 4:
def sum_x (twoFloatTuple: set) -> float:
 """
 The function takes a set of two floating point 
 tuples and returns the sum of the x coordinates 
 of the tuples.
 >>>sum_x({(1.2, 2.8), (2.5, 0.4), (4.1, 1.6))
 7.8
 >>>sum_x({(0, 0), (4.3, -4.76), (4.0, 2.7)})
 8.3
 """
 
 lengthTuple = len(twoFloatTuple)
 
 if lengthTuple == 0:
  return 0
 
 xCoordinateSum = 0
 
 for i in twoFloatTuple:
  xCoordinateSum += i[0]
 return xCoordinateSum

#Main Script:

#Exercise 2:
passCount = 0
failCount = 0

test_int("Testing the 'average' function with listof tuples: ([(27, 219, 134), (0, 0, 0), (1, 2, 30)]):", average([(27, 219, 134), (0, 0, 0), (1, 2, 30)]), [(126, 126, 126), (0, 0, 0), (11, 11, 11)])
test_int("Testing the 'average' function with listof tuples: ([(1, 5, 9), (0, 3, 0), (1, 10, 97)]):", average([(1, 5, 9), (0, 3, 0), (1, 10, 97)]),  [(5, 5, 5), (1, 1, 1), (36, 36, 36)])

print("Exercise 2 passed:", passCount, "time(s)!")
print("Exercise 2 failed:", failCount, "time(s)!\n")   

#Exercise 4:
passCount = 0
failCount = 0

test_int("Testing the 'sum_x' function with list of tuples: {(1.2, 2.8), (2.5, 0.4) and (4.1, 1.6)}:", sum_x({(1.2, 2.8), (2.5, 0.4), (4.1, 1.6)}), 7.8)
test_int("Testing the 'sum_x' function with list of tuples: {(0, 0), (4.3, -4.76), (4.0, 2.7)}:", sum_x({(0, 0), (4.3, -4.76), (4.0, 2.7)}), 8.3)

print("Exercise 4 passed:", passCount, "time(s)!")
print("Exercise 4 failed:", failCount, "time(s)!\n")   
   
   