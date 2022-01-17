#Completed November 17th, 2020
#Last Edited November 17th, 2020
#Author: Nicholai Ponomarev
#Student #101182048

import math

def area_of_disk(radius):
 return math.pi * radius ** 2

def area_of_ring(outer, inner):
 return area_of_disk(outer) - area_of_disk(inner)

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
 return 100* LITRES_PER_GALLON / KMS_PER_MILE / mpg

def accumulated_amount(principal, rate, n, time):
 return principal*(((rate/n)+1)**(n*time))

def area_of_cone(height, radius):
 return (math.pi*radius)*((math.sqrt(radius**2+height**2)))

#Main Script

#Exercise 1:
area = area_of_disk(5)
print(area)
area = area_of_disk(5.0)
print(area)
area = area_of_ring(10, 5)
print(area)
area = area_of_ring(10.0, 5.0)
print(area)

#Exercise 2______________________________________________________________________________________________
print("32 Miles per Gallon is", round(convert_to_litres_per_100_km(32),2), "litres per 100 km!")

#print("0 Miles per Gallon is", convert_to_litres_per_100_km(0), "litres per 100 km!").
#The above line will not work because it is impossible to divide by 0. The error states float division by zero.

print("-5 Miles per Gallon is", round(convert_to_litres_per_100_km(-5),2), "litres per 100 km!")
#The function works for all integer arugments except 0, but it doesnt make sense logically since you cant have negative litres
#per 100 km.

print("1 000 000 Miles per Gallon is", round(convert_to_litres_per_100_km(100000),2), "litres per 100 km!")
#The function works for any inteprint("1 000 000 Miles per Gallon is",convert_to_litres_per_100_km(100000), "litres per 100 km!")

print("Pi Miles per Gallon is", round(convert_to_litres_per_100_km(math.pi),2), "litres per 100 km!")
#The function works for real number number arguments as well!

#Exercise 3:______________________________________________________________________________________________
#Rate is set at 5%, n is set at 4 times (quarterly), time is set for 1 year.
print("If you put in $10 initially, the accumulated amount will be $", round(accumulated_amount(10, 0.05, 4, 1),2), "!")

print("If you put in $0 initially, the accumulated amount will be $", round(accumulated_amount(0, 0.05, 4, 1),2), "!")
#Setting a principal value of $0 still works with no logic errors.

print("If you put in $10 initially, the accumulated amount will be $", round(accumulated_amount(10, 0, 4, 1),2), "!")
#Setting a interest rate of 0.00% still works with no logic errors.

#Exercise 4:______________________________________________________________________________________________
print("If the radius of the cone is 4 cm and the height of the cone is 8 cm, the lateral surface area is", round(area_of_cone(8, 4),2), "cm^2!")

print("If the radius of the cone is -4 cm and the height of the cone is 8 cm, the lateral surface area is", round(area_of_cone(8, -4),2), "cm^2!")

print("If the radius of the cone is 4 cm and the height of the cone is -8 cm, the lateral surface area is", round(area_of_cone(-8, 4),2), "cm^2!")

print("If the radius of the cone is -4 cm and the height of the cone is -8 cm, the lateral surface area is", round(area_of_cone(-8, -4),2), "cm^2!")
#The function works for all negative and postive integers without any mathematical errors. It is however illogical because surface area cannot be negative 
#and neither can radius or height.

print("If the radius of the cone is 0 cm and the height of the cone is 8 cm, the lateral surface area is", round(area_of_cone(-8, 0),2), "cm^2!")

print("If the radius of the cone is 4 cm and the height of the cone is 0 cm, the lateral surface area is", round(area_of_cone(0, -4),2), "cm^2!")

print("If the radius of the cone is 0 cm and the height of the cone is 0 cm, the lateral surface area is", round(area_of_cone(0, 0),2), "cm^2!")
#Inputting a value of 0 does mathematically work however is illogical because if either radius or height is 0, there is no longer a cone. 

print("If the radius of the cone is pi cm and the height of the cone is 5 cm, the lateral surface area is", round(area_of_cone(5, math.pi),2), "cm^2!")
#Inputting a real number argument works as well!