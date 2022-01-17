#Completed December 5th, 2020
#Last Edited December 7th, 2020
#Author: Nicholai Ponomarev
#Student #101182048

#Test Function:
def test_int(testing_message: str, actual_result: int, expected_result: int) -> int:
 """
 This function is designed to shorten the amount of code written.
 Instead off all the different tests done, this function will return 
 a value of 1 if the test is passed or a value of 0 if the test is 
 failed.
 """
 print(testing_message)
 print("Expected result:",expected_result,"Actual result:", actual_result)
 
 if actual_result == expected_result:
  print("Test Passed!")
  global pass_count      #Global must be used so that the variable can be accessed from outside the function.
  pass_count += 1       
  return 1
 
 elif actual_result != expected_result:
  print("Test Failed!")
  global fail_count      #Global must be used so that the variable can be accessed from outside the function.
  fail_count += 1
  return 0
 
#Exercise 1 Function Definition:
def first_last6(list_1: list) -> bool:
 """
 The function takes a non-empty list of integers and returns 
 a value of True if the integer '6' is either the first or last 
 element in the list or both. Otherwise, the function will return
 a value of False.
 >>>first_last6([6, 2, 10, 23, 57])
 True
 >>>first_last6([3, 5, 2, 80, 66, 6])
 True
 >>>first_last6([6, 35, -10, 34, 68, 34948, 6])
 True
 >>>first_list6([1, 2, 3, 4, 5])
 False
 >>>first_list6([1, 6, 6, 6, 6, 6, 1])
 False
 """
 
 target_val = 6
 starting_val_list1 = list_1[0]
 end_val_list1 = list_1[len(list_1)-1]
 
 if starting_val_list1 == target_val:
  return True
 elif end_val_list1 == target_val:
  return True
 else:
  return False
 
#Exercise 2 Function Definition:
def same_first_last(list_1: list) -> bool:
 """
 The takes a list of integers and retrusn True if the list 
 is not empty and if the list has the same first and last 
 elements. Otherwise, it returns false.
 >>>same_first_last([])
 False
 >>>same_first_last([1, 2, 1])
 True
 >>>same_first_last([1, 2, 3, 1, 4])
 False
 """
 
 if (len(list_1) != 0) and (list_1[0] == list_1[len(list_1)-1]):
  return True
 else:
  return False
 
#Exercise 3 Function Definition:
def make_pi() -> list:
 """
 The function has no arguments and simply return a list of length 
 3 containing the first 3 digits of pi.
 >>>make_pi([3, 1, 4])
 [3, 1, 4]
 """
 pi = [3, 1, 4]
 return pi

#Exercise 4 Function Definition:
def common_end(list_1: list, list_2:list) -> bool:
 """
 The function take two non-empty lists that may have varying lengths
 and return True if both lists have the same last or first element of if the 
 first and last elements of both lists are the same. Otherwise, the function will 
 return false.
 >>>common_end([1, 2, 3, 4], [1, 2, 3, 4])
 True
 >>>common_end([1, 2, 3, 4], [2, 3, 4])
 True
 >>>common_end([1, 2, 3, 4], [5, 6, 7, 8])
 False
 >>>common_end([1, 2, 3, 1], [5, 5])
 True
 >>>common_end([1, 2], [1, 2, 3])
 True
 """
 
 if (list_1[0] == list_2[0]):
  return True
 elif (list_1[len(list_1)-1] == list_2[len(list_2)-1]):
  return True
 elif (list_1[0] == list_1[len(list_1)-1]) and (list_2[0] == list_2[len(list_2)-1]):
  return True
 else: 
  return False

#Exercise 5 Function Definition:
def sum_3(int_3_list: list) -> int:
 """
 The function takes a list containing three integers
 and return the sum of the integers.
 >>>sum_3([1, 2, 3])
 6
 >>>sum_3([0, 0, 0])
 0
 >>>sum_3([-1, -2, 20])
 17
 """
 
 return sum(int_3_list)

#Exercise 6 Function Definition:
def rotate_left3(int_3_list: list) -> list:
 """
 This function takes a list of 3 integers and rotates the list left.
 [4, 6, 5].
 >>>rotate_left3([5, 4, 6])
 [4, 6, 5]
 >>>rotate_left3([1, 0, 3])
 [0, 3, 1]
 >>>rotate_left3([0, -1, 0])
 [-1, 0, 0]
 """
 
 return [int_3_list[1], int_3_list[2], int_3_list[0]]

#Exercise 7 Function Definition:
def reverse3(int_3_list: list) -> list:
 """
 This function takes a list of 3 integers and reverses them
 in order.
 >>>reverse3([1, 2, 3])
 [3, 2, 1]
 >>>reverse3([4, 3, 6])
 [6, 3, 4]
 >>>reverse3([0, -1, 0])
 [0, -1, 0]
 """
 
 return [int_3_list[2], int_3_list[1], int_3_list[0]]

#Exercise 8 Function Definition:
def max_end3(max_end3: list) -> list:
 """
 The function takes a list with three elements and determines wether
 the first value or the last value is larger. It them initiallizes
 the list to that larger value.
 >>>max_end3([1, 2, 4])
 [4, 4, 4]
 >>>max_end([3, 2, 1])
 [3, 3, 3]
 >>>max_end([-1, 3, -2])
 [-1, -1, -1]
 """
 
 if max_end3[0] > max_end3[2]:
  return [max_end3[0], max_end3[0], max_end3[0]]
 elif max_end3[0] < max_end3[2]:
  return [max_end3[2], max_end3[2], max_end3[2]]
 
#Exercise 9 Function Definition:
def sum2(list_1: list) -> int:
 """
 The function takes a list of integers return the sum of the first 
 two elements in the list. The function returns 0 if the list is empty
 or if the list only has 1 element.
 >>>sum2([1, 2, 4])
 3
 >>>sum2([])
 0
 >>>sum2([1, -5, 5, 7])
 -4
 >>>sum2([1])
 0
 """
 
 min_length = 2
 
 if len(list_1) >= min_length:
  return list_1[0] + list_1[1]
 else:
  return 0
 
#Exercise 10 Function Definition:
def middle_way(int_3_list1: list, int_3_list2: list) -> list:
 """
 Teh function takes two lists of 3 integers each and returns a list
 containing the middle elements of the two original lists.
 >>>middle_way([1, 2, 3], [4, 5, 6])
 [2, 5]
 >>>middle_way([0, 0, 0], [0, 1, 0])
 [0, 1]
 >>>middle_way([-1, -2, -3], [1, 2, 4])
 [-2, 2]
 """
 
 return [int_3_list1[1], int_3_list2[1]]

#Exercise 11 Function Definition:
def make_ends(non_empty_list: list) -> list:
 """
 The function takes a non-empty list of integers and returns
 a new list containing the original lists first and last elements.
 >>>make_ends([4, 5, 6, 7])
 [4, 7]
 >>>make_ends([1, 2, 4])
 [1, 4]
 >>>make_ends([0, -1, 0])
 [0, 0]
 """
 
 return [non_empty_list[0], non_empty_list[len(non_empty_list)-1]]

#Exercise 12 Function Definition:
def has23(int_2_list: list) -> bool:
 """
 This function takes a list containing two integers and returns 
 True if the list contains either a 2 or a 3 or both. Otherwise it 
 returns False.
 >>>has23([1, 2])
 True
 >>>has23([2, 4])
 True
 >>>has23([3, 3])
 True
 >>>has23([-2, -3])
 False
 """
 
 element_1 = int_2_list[0]
 element_2 = int_2_list[1]
 
 if element_1 == 2 or element_2 == 2:
  return True
 elif element_1 == 3 or element_2 == 3:
  return True
 else:
  return False

#Main Script:

#Exericse 1:
pass_count = 0
fail_count = 0

test_int("Testing the 'first_last6' function with list [6, 2, 10, 23, 57]:", first_last6([6, 2, 10, 23, 57]), True)
test_int("Testing the 'first_last6' function with list [3, 5, 2, 80, 66, 6]:", first_last6([3, 5, 2, 80, 66, 6]), True)
test_int("Testing the 'first_last6' function with list [6, 35, -10, 34, 68, 34948, 6]:", first_last6([6, 35, -10, 34, 68, 34948, 6]), True)
test_int("Testing the 'first_last6' function with list [1, 2, 3, 4, 5]:", first_last6([1, 2, 3, 4, 5]), False)
test_int("Testing the 'first_last6' function with list [1, 6, 6, 6, 6, 6, 1]:", first_last6([1, 6, 6, 6, 6, 6, 1]), False)

print("Exercise 1 passed:", pass_count, "time(s)!")
print("Exercise 1 failed:", fail_count, "time(s)!\n")

#Exercise 2:
pass_count = 0
fail_count = 0

test_int("Testing the 'same_first_last' function with list []:", same_first_last([]), False)
test_int("Testing the 'same_first_last' function with list [1, 2, 1]:", same_first_last([1, 2, 1]), True)
test_int("Testing the 'same_first_last' function with list [1, 2, 3, 1, 4]:", same_first_last([1, 2, 3, 1, 4]), False)

print("Exercise 2 passed:", pass_count, "time(s)!")
print("Exercise 2 failed:", fail_count, "time(s)!\n")

#Exercise 3:
print("Testing the 'make_pi' function:", make_pi(), "\n")

#Exercise 4:
pass_count = 0
fail_count = 0

test_int("Testing the 'common_end' function with list_1 [1, 2, 4, 4] and list_2 [1, 2, 3, 4]:", common_end([1, 2, 3, 4], [1, 2, 3, 4]), True)
test_int("Testing the 'common_end' function with list_1 [1, 2, 4, 4] and list_2 [2, 3, 4]:", common_end([1, 2, 3, 4], [2, 3, 4]), True)
test_int("Testing the 'common_end' function with list_1 [1, 2, 4, 4] and list_2 [5, 6, 7, 8]:", common_end([1, 2, 3, 4], [5, 6, 7, 8]), False)
test_int("Testing the 'common_end' function with list_1 [1, 2, 4, 1] and list_2 [5, 5]:", common_end([1, 2, 3, 1], [5, 5]), True)
test_int("Testing the 'common_end' function with list_1 [1, 2] and list_2 [1, 2, 3]:", common_end([1, 2], [1, 2, 3]), True)

print("Exercise 4 passed:", pass_count, "time(s)!")
print("Exercise 4 failed:", fail_count, "time(s)!\n")

#Exercise 5:
pass_count = 0
fail_count = 0

test_int("Testing the 'sum_3' function with list [1, 2, 3]:", sum_3([1, 2, 3]), 6)
test_int("Testing the 'sum_3' function with list [0, 0, 0]:", sum_3([0, 0, 0]), 0)
test_int("Testing the 'sum_3' function with list [-1, -2, 20]:", sum_3([-1, -2, 20]), 17)

print("Exercise 5 passed:", pass_count, "time(s)!")
print("Exercise 5 failed:", fail_count, "time(s)!\n")

#Exercise 6:
pass_count = 0
fail_count = 0

test_int("Testing the 'rotate_left3' function with list [5, 4, 6]:", rotate_left3([5, 4, 6]), [4, 6, 5])
test_int("Testing the 'rotate_left3' function with list [0, 3, 1]:", rotate_left3([0, 3, 1]), [3, 1, 0])
test_int("Testing the 'rotate_left3' function with list [-1, 0, 0]:", rotate_left3([-1, 0, 0]), [0, 0, -1])

print("Exercise 6 passed:", pass_count, "time(s)!")
print("Exercise 6 failed:", fail_count, "time(s)!\n")

#Exercise 7:
pass_count = 0
fail_count = 0

test_int("Testing the 'reverse3' function with list [1, 2, 3]:", reverse3([1, 2, 3]), [3, 2, 1])
test_int("Testing the 'reverse3' function with list [4, 3, 6]:", reverse3([4, 3, 6]), [6, 3, 4])
test_int("Testing the 'reverse3' function with list [0, -1, 0]:", reverse3([0, -1, 0]), [0, -1, 0])

print("Exercise 7 passed:", pass_count, "time(s)!")
print("Exercise 7 failed:", fail_count, "time(s)!\n")

#Exercise 8:
pass_count = 0
fail_count = 0

test_int("Testing the 'max_end3' function with list [1, 2, 4]:", max_end3([1, 2, 4]), [4, 4, 4])
test_int("Testing the 'max_end3' function with list [3, 2, 1]:", max_end3([3, 2, 1]), [3, 3, 3])
test_int("Testing the 'max_end3' function with list [-1, 3, -2]:", max_end3([-1, 3, -2]), [-1, -1, -1])

print("Exercise 8 passed:", pass_count, "time(s)!")
print("Exercise 8 failed:", fail_count, "time(s)!\n")

#Exercise 9:
pass_count = 0
fail_count = 0

test_int("Testing the 'sum2' function with list [1, 2, 4]:", sum2([1, 2, 4]), 3)
test_int("Testing the 'sum2' function with list []:", sum2([]), 0)
test_int("Testing the 'sum2' function with list [1, -5, 5, 7]:", sum2([1, -5, 5, 7]), -4)
test_int("Testing the 'sum2' function with list [1]:", sum2([1]), 0)

print("Exercise 9 passed:", pass_count, "time(s)!")
print("Exercise 9 failed:", fail_count, "time(s)!\n")

#Exercise 10;
pass_count = 0
fail_count = 0

test_int("Testing the 'middle_way' function with int_3_list1 [1, 2, 3] and int_3_list2 [4, 5, 6]:", middle_way([1, 2, 3], [4, 5, 6]), [2, 5])
test_int("Testing the 'middle_way' function with int_3_list1 [0, 0, 0] and int_3_list2 [0, 1, 0]:", middle_way([0, 0, 0], [0, 1, 0]), [0, 1])
test_int("Testing the 'middle_way' function with int_3_list1 [-1, -2, -3] and int_3_list2 [1, 2, 4]:", middle_way([-1, -2, -3], [1, 2, 4]), [-2, 2])

print("Exercise 10 passed:", pass_count, "time(s)!")
print("Exercise 10 failed:", fail_count, "time(s)!\n")

#Exercise 11:
pass_count = 0
fail_count = 0

test_int("Testing the 'make_ends' function with list [4, 5, 6, 7]:", make_ends([4, 5, 6, 7]), [4, 7])
test_int("Testing the 'make_ends' function with list [1, 2, 4]:", make_ends([1, 2, 4]), [1, 4])
test_int("Testing the 'make_ends' function with list [0, -1, 0]:", make_ends([0, -1, 0]), [0, 0])

print("Exercise 11 passed:", pass_count, "time(s)!")
print("Exercise 11 failed:", fail_count, "time(s)!\n")

#Exercise 12:
pass_count = 0
fail_count = 0

test_int("Testing the 'has23' function with list [1, 2]:", has23([1, 2]), True)
test_int("Testing the 'has23' function with list [2, 4]:", has23([2, 4]), True)
test_int("Testing the 'has23' function with list [3, 3]:", has23([3, 3]), True)
test_int("Testing the 'has23' function with list [-3, -3]:", has23([-3, -3]), False)

print("Exercise 12 passed:", pass_count, "time(s)!")
print("Exercise 12 failed:", fail_count, "time(s)!\n")
