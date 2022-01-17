#Completed December 8th, 2020
#Last Edited December 11th, 2020
#Author: Nicholai Ponomarev
#Student #101182048

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
  passCount += 1       
  return 1
 
 elif actualResult != expectedResult:
  print("Test Failed!")
  global failCount      #Global must be used so that the variable can be accessed from outside the function.
  failCount += 1
  return 0
 
#Exercise 1 Function Definition:
def count_evens(intList: list) -> int:
 """
 The function takes a list of integers which may be empty
 and return the number of even integers the list contains.
 >>>count_evens([1, 2, 3, 4, 5])
 2
 >>>count_evens([])
 0
 >>>count_evens([1, 3, 5, 7])
 0
 >>>count_evens([-2, -100, 0, 4])
 4
 """
 
 evenNum = 0   #camelCase Variable name instead of list_length. Personal Preference.
 
 if len(intList)>0:
  for i in range(len(intList)):
   if intList[i] % 2 == 0:
    evenNum +=1 
  return evenNum
 
 if len(intList) == 0:
  return 0
 
#Exercise 2 Function Definition:
def big_diff(intList: list) -> int:
 """
 The function takes a list of atleast two integers and 
 returns the difference between the smallest and biggest integers.
 I personally added a little touch that if the list is under 2 integers 
 long, the function automatically returns 0.
 >>>big_diff([10, 3, 5, 6])
 7
 >>>big_diff([1, 2, 3, 5])
 4
 >>>big_diff([-1, -2, 10, -5])
 15
 >>>big_diff([0, 0])
 0
 """
 
 reference_MAX_int = intList[0]
 reference_MIN_int = intList[0]
 
 listLength = len(intList) 
 
 count = 1
 
 if listLength < 2:
  return 0
 
 while count < listLength:
  if intList[count] > reference_MAX_int:
   reference_MAX_int = intList[count]
  elif intList[count] < reference_MIN_int:
   reference_MIN_int = intList[count]
  count += 1
 return reference_MAX_int - reference_MIN_int
 
#Exercise 3 Function Definition:
def has22(intList:list) -> bool:
 """
 The function takes a list of integers which may be empty and 
 return True if the list contains two '2' beside eachother, otherwise,
 the function returns False.
 >>>has22([1,2,2,4])
 True
 >>>has22([])
 False
 >>>has22([1, 2, 3, 2])
 False
 >>>has22([-1, -2, -2, 2, 2, 5])
 True
 """

 for i in range(len(intList)):
     targetNum = 2
     first2 = intList[i]
     second2 = intList[i-1]
     if (first2 == targetNum ) and (second2 == targetNum ):
         return True
 return False

#Exercise 4 Function Definition:
def centered_average(intList: list) -> float:
 """
 The function takes a list of atleast three integers and 
 computes their centered average. It then returns the 
 computed centred average.
 >>>centered_average([1, 1, 5, 5, 10, 8, 7])
 5.2
 >>>centered_average([1, 2, 5, 10, 6, 5])
 4.5
 >>>centered_average([-1, -1, 10, 10, 3])
 4.0
 >>>centered_average([-1, -1, -1000, 37564, -182940, 2])
 -250.0
 """
 
 sumInt = 0
 
 for i in intList:
  sumInt = sumInt + i
  lenth = len(intList)
  maxInt = max(intList)
  minInt = min(intList)  
 return round((sumInt - maxInt - minInt) / (lenth - 2),2) 

#Exercise 5 Function Definition:
def sum13(intList: list) -> int:
 """
 The function takes a list of integers which may be empty. It returns 
 the sum of the list if there is no 13. If there is a 13, it returns the sum 
 of the list but excludes 13 and any number immediately after 13 in the calculations.
 >>>sum13([1, 2, 2, 1, 13])
 6
 >>>sum([13, 1, 2, 13, 2, 1, 13])
 3
 >>>sum13([])
 0
 >>>sum13([1, 2, 3, 4, 10, 13, 1])
 20
 """
 
 sumInt = 0
 
 if len(intList) == 0:
  return 0
 
 for i in range(0, len(intList)):
  if intList[i] == 13:
   intList[i] = 0
   if len(intList) > i + 1:
    intList[i+1] = 0
    
 for i in intList:
  sumInt = sumInt +i
 return round(sumInt,1)

#Exercise 6 Function Definition
def sum67(intList: list) -> int:
 """
 The function takes a list of integers which may be empty
 and returns the sum of the list or 0 if the list is empty. 
 The function will ignore any sequences of numbers starting 
 with 6 and ending with 7 inclusively in the calculation.
 >>>sum67([1, 2, 2, 6, 99, 99, 7])
 5
 >>>sum67([])
 0
 >>>sum67([6, 8, 7])
 0
 >>>sum67([-1, -10, 6, 3, 4, 7, 29])
 18
 """
 
 sumInt = 0
 stopCounting = False
 
 if len(intList) == 0:
  return 0
 
 for i in intList:
  if i == 6:
   stopCounting = True
  elif i == 7:
   stopCounting = False
  elif stopCounting is False:
   sumInt += i
 return sumInt

#Exercise 7 Function Definition
def bank_statement(floatList: list) -> list:
 """
 The function takes a list of floating point values represent money amounts.
 Positive values represent bank deposits and negative numbers represent bank 
 withdrawls. The function will return a new list containing three floating point
 values. The first one is total deposits, the second one is total withdrawls, and 
 third one is total account balance so the sum of the first two.
 >>>bank_statment([0.00])
 [0.00, 0.00, 0.00]
 >>>bank_statement([340.26, 476.97, -321.85, 52.47])
 [869.70, -321.85, 547.85]
 >>>bank_statement([-340.26, -476.97, -321.85, -52.47])
 [0.00, -1191.55, -1191.55]
 """
 
 depositSum = 0
 withdrawlSum = 0
 
 for i in floatList:
  if i > 0:
   depositSum += i
  else:
   withdrawlSum += i
   
 finalBalance = round(depositSum,2) + round(withdrawlSum,2)
 
 return [depositSum, withdrawlSum, round(finalBalance,2)]

#Exercise 8 Function Definition:
def divisors(posInt: int) -> list:
 """
 The functions takes a positive integers with name "pos_int"
 and returns a list of all the possible divisors of "pos_int".
 >>>divisors(6)
 [6, 3, 2, 1]
 >>>divisors(10)
 [10, 5, 2, 1]
 >>>divisors(9)
 [9, 3, 1]
 """
 
 divisors = []
 divCheck = posInt
 
 while divCheck > 0:
  if (posInt % divCheck) == 0:
   divisors = divisors + [divCheck]
  divCheck -= 1
 return divisors 

#Exercise 9 Function Definition:
def reverse(list1:list) -> list:
 """
 The function takes a list which can be empty and returns a new list 
 that contains all the elements in the original list in a reversed order.
 >>>reverse([4, 2, 3, 2])
 [2, 3, 2, 4]
 >>>reverse([1, 2, 3, 4, 5])
 [5, 4, 3, 2, 1]
 >>>reverse([])
 []
 >>>reverse([-1, 3, 4, 100, -10])
 [-10, 100, 4, 3, -1]
 """
 
 lengthList = len(list1)
 
 intialReversedList = [None]*lengthList  #Creates an list with the same amount of elements as the first list.
 
 for element in list1:
  lengthList = lengthList-1
  intialReversedList[lengthList] = element
 return intialReversedList

#Main Script:

#Exercise 1:
passCount = 0
failCount = 0

test_int("Testing the 'count_evens' function with list [1, 2, 3, 4, 5]:", count_evens([1, 2, 3, 4, 5]), 2)
test_int("Testing the 'count_evens' function with list []:", count_evens([]), 0)
test_int("Testing the 'count_evens' function with list [1, 3, 5, 7]:", count_evens([1, 3, 5, 7]), 0)
test_int("Testing the 'count_evens' function with list [-2, -100, 0, 4]:", count_evens([-2, -100, 0, 4]), 4)

print("Exercise 1 passed:", passCount, "time(s)!")
print("Exercise 1 failed:", failCount, "time(s)!\n")   
    
#Exercise 2:
passCount = 0
failCount = 0

test_int("Testing the 'big_diff' function with list [10, 3, 5, 6]:", big_diff([10, 3, 5, 6]), 7)
test_int("Testing the 'big_diff' function with list [1, 2, 3, 5]:", big_diff([1, 2, 3, 5]), 4)
test_int("Testing the 'big_diff' function with list [-1, -2, 10, -5]:", big_diff([-1, -2, 10, -5]), 15)
test_int("Testing the 'big_diff' function with list [0, 0]:", big_diff([0, 0]), 0)

print("Exercise 2 passed:", passCount, "time(s)!")
print("Exercise 2 failed:", failCount, "time(s)!\n")   

#Exercise 3:
passCount = 0
failCount = 0

test_int("Testing the 'has22' function with list [1, 2, 2, 4]:", has22([1, 2, 2, 4]), True)
test_int("Testing the 'has22' function with list []:", has22([]), False)
test_int("Testing the 'has22' function with list [-1, -2, 3, 2]:", has22([-1, -2, 3, 2]), False)
test_int("Testing the 'has22' function with list [-1, -2, -2, 2, 2, 5]:", has22([-1, -2, -2, 2, 2, 5]), True)

print("Exercise 3 passed:", passCount, "time(s)!")
print("Exercise 3 failed:", failCount, "time(s)!\n")   

#Exercise 4:
passCount = 0
failCount = 0

test_int("Testing the 'centered_average' function with list [1, 1, 5, 5, 10, 8, 7]:", centered_average([1, 1, 5, 5, 10, 8, 7]), 5.2)
test_int("Testing the 'centered_average' function with list [1, 2, 5, 10, 6, 5]:", centered_average([1, 2, 5, 10, 6, 5]), 4.5)
test_int("Testing the 'centered_average' function with list [-1, -1, 10, 10, 3]:", centered_average([-1, -1, 10, 10, 3]), 4.0)
test_int("Testing the 'centered_average' function with list [-1, -1, -1000, 37564, -182940, 2]:", centered_average([-1, -1, -1000, 37564, -182940, 2]), -250.0)


print("Exercise 4 passed:", passCount, "time(s)!")
print("Exercise 4 failed:", failCount, "time(s)!\n")   

#Exercise 5:
passCount = 0
failCount = 0

test_int("Testing the 'sum13' function with list [1, 1, 5, 5, 10, 8, 7]:", sum13([1, 2, 2, 1]), 6)
test_int("Testing the 'sum13' function with list [13, 1, 2, 13, 2, 1, 13]:", sum13([13, 1, 2, 13, 2, 1, 13]), 3)
test_int("Testing the 'sum13' function with list []:", sum13([]), 0)
test_int("Testing the 'sum13' function with list [1, 2, 3, 4, 10, 13, 1]:", sum13([1, 2, 3, 4, 10, 13, 1]), 20)

print("Exercise 5 passed:", passCount, "time(s)!")
print("Exercise 5 failed:", failCount, "time(s)!\n")   

#Exercise 6:
passCount = 0
failCount = 0

test_int("Testing the 'sum67' function with list [1, 2, 2, 6, 99, 99, 7]:", sum67([1, 2, 2, 6, 99, 99, 7]), 5)
test_int("Testing the 'sum67' function with list []:", sum67([]), 0)
test_int("Testing the 'sum67' function with list [6, 8, 7]:", sum67([6, 8, 7]), 0)
test_int("Testing the 'sum67' function with list [-1, -10, 6, 3, 4, 7, 29]:", sum67([-1, -10, 6, 3, 4, 7, 29]), 18)

print("Exercise 6 passed:", passCount, "time(s)!")
print("Exercise 6 failed:", failCount, "time(s)!\n")   

#Exercise 7:
passCount = 0
failCount = 0

test_int("Testing the 'bank_statement' function with list [0.00]:", bank_statement([0.00]), [0.00, 0.00, 0.00])
test_int("Testing the 'bank_statement' function with list [340.26, 476.97, -321.85, 52.47]:", bank_statement([340.26, 476.97, -321.85, 52.47]), [869.70, -321.85, 547.85])
test_int("Testing the 'bank_statement' function with list [-340.26, -476.97, -321.85, -52.47]:", bank_statement([-340.26, -476.97, -321.85, -52.47]), [0.00, -1191.55, -1191.55])
        
print("Exercise 7 passed:", passCount, "time(s)!")
print("Exercise 7 failed:", failCount, "time(s)!\n")    

#Exercise 8:
passCount = 0
failCount = 0

test_int("Testing the 'divisors' function with positive integer 6:", divisors(6), [6, 3, 2, 1])
test_int("Testing the 'divisors' function with positive integer 10:", divisors(10), [10, 5, 2, 1])
test_int("Testing the 'divisors' function with positive integer 9:", divisors(9), [9, 3, 1])

print("Exercise 8 passed:", passCount, "time(s)!")
print("Exercise 8 failed:", failCount, "time(s)!\n")    

#Exercise 9:
passCount = 0
failCount = 0

test_int("Testing the 'reverse' function with list1 [4, 2, 3, 2] :", reverse([4, 2, 3, 2]), [2, 3, 2, 4])
test_int("Testing the 'reverse' function with list1 [1, 2, 3, 4, 5] :", reverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
test_int("Testing the 'reverse' function with list1 [] :", reverse([]), [])
test_int("Testing the 'reverse' function with list1 [-1, 3, 4, 100, -10] :", reverse([-1, 3, 4, 100, -10]), [-10, 100, 4, 3, -1])

print("Exercise 9 passed:", passCount, "time(s)!")
print("Exercise 9 failed:", failCount, "time(s)!\n") 
