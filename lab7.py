#Completed November 24th, 2020
#Last Edited November 29th, 2020
#Author: Nicholai Ponomarev
#Student #101182048

#Excercise 1 Function Definition:
def factorial(n: int) -> int:
 """Return n! for positive values of n.
 >>> factorial(1)
 1
 >>> factorial(2)
 2
 >>> factorial(3)
 6
 >>> factorial(4)
 24
 """
 fact = 1
 for i in range(2,n+1):
  fact = fact * n

 return fact 

#Excerise 2 Function Definition:
def tip(cost_of_meal: float, satisfaction_level: int) -> float:
 """
 Returns a suggested tip value based on the customers 
 total cost of meal and satisfaction level.
 >>>tip(15.00, 3)
 0.75
 >>>tip(20.64, 1)
 4.13
 >>>tip(-0.45, -2)
 Invalid Input!
 """
 
 if satisfaction_level == 1:
  tip_percentage = 0.20
 elif satisfaction_level == 2:
  tip_percentage = 0.10
 elif satisfaction_level == 3:
  tip_percentage = 0.05
  
 return round(cost_of_meal*tip_percentage,2)

#Excercise 3 Function Definition:
def coupon(amount_spent_on_groceries: float) -> float:
 """
 Returns a coupon value based on the dollar 
 amount spent on groceries.
 >>>coupon(5.00)
 No Coupon
 >>>coupon(35.65)
 2.85
 >>>coupon(213.50)
 29.89
 """
 
 if amount_spent_on_groceries<10.00:
  coupon_percentage = 0
 elif 10.00<=amount_spent_on_groceries<=60.00:
  coupon_percentage = 0.08
 elif 60.00<amount_spent_on_groceries<=150.00:
  coupon_percentage = 0.10
 elif 150.00<amount_spent_on_groceries<=210.00:
  coupon_percentage = 0.12
 elif amount_spent_on_groceries>210.00:
  coupon_percentage = 0.14
 return round(amount_spent_on_groceries*coupon_percentage,2)

#Final Excercise Test Function Definition:
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
  
#Main Script:
#Excercise 1:
#New Code:

pass_count = 0
fail_count = 0

test_int("Testing factorial(1):",1,factorial(1))
test_int("Testing factorial(2):",2,factorial(2))
test_int("Testing factorial(3):",6,factorial(3))
test_int("Testing factorial(4):",24,factorial(4))

print(pass_count, "tests passed for Exercise 1!")
print(fail_count, "tests failed for Exercise 1!")

#Replaced Code:
"""
pass_count = 0
fail_count = 0

result = factorial(1)
print("Testing factorial(1)")
print("Expected result: 1 Actual result:", result)
if result == 1:
 print("Test Passed")
 pass_count += 1
else:
 print("Test Failed")
 fail_count +=1
 
result = factorial(2)
print("Testing factorial(2)")
print("Expected result: 2 Actual result:", result)
if result == 2:
 print("Test Passed")
 pass_count += 1
else:
 print("Test Failed")
 fail_count +=1
 
result = factorial(3)
print("Testing factorial(3)")
print("Expected result: 6 Actual result:", result)
if result == 6:
 print("Test Passed")
 pass_count += 1
else:
 print("Test Failed")
fail_count +=1

result = factorial(4)
print("Testing factorial(4)")
print("Expected result: 24 Actual result:", result)
if result == 24:
 print("Test Passed")
 pass_count += 1
else:
 print("Test Failed")
fail_count +=1

print(pass_count, "tests passed for Exercise 1!")
print(fail_count, "tests failed for Exercise 1!")
"""

#Exercise 2:
pass_count = 0
fail_count = 0

total_tip = tip(15.00,1)
print("Testing for 1st arguments:")
print("Expected result: 3.0 Actual Result:",total_tip)
if total_tip == 3.0:
 print("Test Passed!")
 pass_count += 1
else:
 print("Test Failed!")
 fail_count +=1
 
total_tip = tip(20.64,2)
print("Testing for 2nd arguments:")
print("Expected result: 2.06 Actual Result:",total_tip)
if total_tip == 2.06:
 print("Test Passed!")
 pass_count += 1
else:
 print("Test Failed!")
 fail_count +=1
 
total_tip = tip(43.25,3)
print("Testing for 3rd arguments:")
print("Expected result: 2.16 Actual Result:",total_tip)
if total_tip == 2.16:
 print("Test Passed!")
 pass_count += 1
else:
 print("Test Failed!")
 fail_count +=1
 
print(pass_count, "test passed for Exercise 2!")
print(fail_count, "tests failed for Exercise 2!")

#Excercise 3:
#Shorter and More Concise code with "test" function:
pass_count = 0
fail_count = 0

test_int("Testing total coupon value with $5.00 purchase:",0.00,coupon(5.00))
test_int("Testing total coupon value with $25.00 purchase:",2.00,coupon(25.00))
test_int("Testing total coupon value with $74.65 purchase:",7.47,coupon(74.65))
test_int("Testing total coupon value with $175.00 purchase:",21.00,coupon(175.00))
test_int("Testing total coupon value with $235.00 purchase:",32.90,coupon(235.00))


print(pass_count, "tests passed for Exercise 3!")
print(fail_count, "tests failed for Exercise 3!")

#Replaced Code
"""
pass_count = 0
fail_count = 0

total_coupon_value = coupon(5.00)
print("Testing for 1st value:")
print("Expected result: 0.00 Actual Result:",total_coupon_value)
if total_coupon_value == 0.00:
 print("Test Passed!")
 pass_count += 1
else:
 print("Test Failed!")
 fail_count +=1
 
total_coupon_value = coupon(35.65)
print("Testing for 2nd value:")
print("Expected result: 2.85 Actual Result:",total_coupon_value)
if total_coupon_value == 2.85:
 print("Test Passed!")
 pass_count += 1
else:
 print("Test Failed!")
 fail_count +=1
 
total_coupon_value = coupon(213.50)
print("Testing for 3rd value:")
print("Expected result: 29.89 Actual Result:",total_coupon_value)
if total_coupon_value == 29.89:
 print("Test Passed!")
 pass_count += 1
else:
 print("Test Failed!")
 fail_count +=1
 
print(pass_count, "test passed for Exercise 3!")
print(fail_count, "tests failed for Exercise 3!")
"""

 
 