#Completed December 1st, 2020
#Last Edited December 2nd, 2020
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
def bakers_party(num_pastries: int, day_type: bool) -> bool:
 """
 This function returns True if the the bakers baked between 40 and 60 pastries
 on a weekday. The function also returns True if the baker baked more than or exactly
 40 pastries on the weekend. The function returns False if the above isn't True.
 >>>bakers_party(45, True)
 True
 >>>bakers_party(15, True)
 False
 >>>bakers_party(61, False)
 False
 >>>bakers_party(105, True)
 True
 >>>bakers_party(20, False)
 False
 """
 
 min_number = 40
 max_number_weekday = 60
 
 if num_pastries>=min_number and day_type == True:
  return True
 elif min_number<=num_pastries<=max_number_weekday and day_type == False:
  return True
 else:
  return False
 
#Exercise 2 Function Definition:
def squirrel_play(temperature:int, season_type:bool) -> bool:
 """
 Returns True or False if the given arguments which temperature of the time
 and the type of season it is are proven to be successful.
 >>>squirrel_play(75, True)
 True
 >>>squirrel_play(15, False)
 False
 >>>squirrel_play(100, True)
 True
 >>>squirrel_play(60, False)
 True
 """
 min_temp = 60
 max_temp_summer = 100
 max_temp_other = 90
 if min_temp<=temperature<=max_temp_summer and season_type == True:
  return True
 elif min_temp<=temperature<=max_temp_other and season_type == False:
  return True
 else:
  return False
 
#Exercise 3 Function Definition:
def great_42(a: int, b: int) -> bool:
 """
 Returns True if the the value for either a or b is 42
 or if the sum or difference of a and b is 42. Returns false
 if none of the above statements are True.
 >>>great_42(42,6)
 True
 >>>great_42(72, 30)
 True
 >>>great_42(41,2)
 False
 >>>great_42(21, 21)
 True
 """
 
 target_value = 42
 
 if a == target_value or a+b == target_value or abs(a-b) == target_value:
  return True
 elif b == target_value:
  return True
 else:
  return False
 
#Exercise 4 Function Definition:
def blackjack(a: int, b: int) -> int:
 """Returns the closest value to 21 between the variables a and b. If the 
 one of the values is over 21, the function automatically returns the 
 value that is under 21. If both values are over 21, the function returns 0.
 >>>blackjack(12,17)
 17
 >>>blackjack(12,22)
 12
 >>>blackjack(22,23)
 0
 >>>blackjack(21,21)
 21
 >>>blackjack(23,21)
 21
 """
 
 blackjack_target = 21

 if a>b and a<=blackjack_target:
  return a
 elif b>a and b<=blackjack_target:
  return b
 elif b>blackjack_target and a<=blackjack_target:
  return a
 elif a>blackjack_target and b<=blackjack_target:
  return b
 elif a == b and a<=blackjack_target and b<=blackjack_target:
  return a
 elif a>blackjack_target and b>blackjack_target:
  return 0
 
#Exercise 5 Function Definition:
def sum_uniques(a: int, b:int, c:int) -> int:
 """Returns the sum of the three integers a, b and c if they are 
 all unique. If two are alike, they will not be used when calculating the sum.
 If the three integers are identical in value, the function returns a sum  of 0.
 >>>sum_uniques(1,2,3)
 6
 >>>sum_uniques(1,-2,10)
 9
 >>>sum_uniques(1,2,2)
 1
 >>>sum_uniques(1,1,3)
 3
 >>>sum_uniques(1,2,1)
 2
 >>>sum_uniques(3,3,3)
 0
 """
 
 if a != b and b != c and c != a:
  return a+b+c
 elif a == b and c != a:
  return c
 elif b == c and a != b:
  return a
 elif a == c and b != a:
  return b
 elif a == b and b == c:
  return 0
 
 
#Main Script:
 
#Exericse 1:
pass_count = 0
fail_count = 0

test_int("Testing the 'bakers_party' function(45, True):", bakers_party(45, True), True)
test_int("Testing the 'bakers party' function(15, True):", bakers_party(15, True), False)
test_int("Testing the 'bakers party' function(61, False):", bakers_party(61, False), False)
test_int("Testing the 'bakers party' function(105, True):", bakers_party(105, True), True)
test_int("Testing the 'bakers party' function(20, False):", bakers_party(20, False), False)

print("The test for Exercise 1 passed", pass_count, "time(s)!")
print("The test for Exercise 1 failed", fail_count, "time(s)!\n")

#Exercise 2:
pass_count = 0
fail_count = 0

test_int("Testing the 'squirrel_play' function(75, True):", squirrel_play(75, True), True)
test_int("Testing the 'squirrel play' function(15, False):", squirrel_play(15, False), False)
test_int("Testing the 'squirrel play' function(100, True):", squirrel_play(100, True), True)
test_int("Testing the 'squirrel play' function(60, False):", squirrel_play(60, False), True)

print("The test for Exercise 2 passed", pass_count, "time(s)!")
print("The test for Exercise 2 failed", fail_count, "time(s)!\n")

#Exercise 3:
pass_count = 0
fail_count = 0

test_int("Testing the 'great_42' function(42,6):", great_42(42,6), True)
test_int("Testing the 'great_42' function(72, 30):", great_42(72, 30), True)
test_int("Testing the 'great_42' function(41, 2):", great_42(41, 2), False)
test_int("Testing the 'great_42' function(21, 21):", great_42(21, 21), True)

print("The test for Exercise 3 passed", pass_count, "time(s)!")
print("The test for Exercise 3 failed", fail_count, "time(s)!\n")

#Exercise 4:
pass_count = 0
fail_count = 0

test_int("Testing the 'blackjack' function(12,17):", blackjack(12,17), 17)
test_int("Testing the 'blackjack' function(12,22):", blackjack(12,22), 12)
test_int("Testing the 'blackjack' function(22,23):", blackjack(22,23), 0)
test_int("Testing the 'blackjack' function(12,17):", blackjack(21,21), 21)
test_int("Testing the 'blackjack' function(12,17):", blackjack(23,21), 21)


print("The test for Exercise 4 passed", pass_count, "time(s)!")
print("The test for Exercise 4 failed", fail_count, "time(s)!\n")

#Exercise 5:
pass_count = 0
fail_count = 0

test_int("Testing the 'sum_uniques' function(1,2,3):", sum_uniques(1,2,3), 6)
test_int("Testing the 'sum_uniques' function(1,-2,10):", sum_uniques(1,-2,10), 9)
test_int("Testing the 'sum_uniques' function(1,2,2):", sum_uniques(1,2,2), 1)
test_int("Testing the 'sum_uniques' function(1,1,3):", sum_uniques(1,1,3), 3)
test_int("Testing the 'sum_uniques' function(1,2,1):", sum_uniques(1,2,1), 2)
test_int("Testing the 'sum_uniques' function(3,3,3):", sum_uniques(3,3,3), 0)

print("The test for Exercise 5 passed", pass_count, "time(s)!")
print("The test for Exercise 5 failed", fail_count, "time(s)!\n")