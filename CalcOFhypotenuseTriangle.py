#Python program to calculate the hypotenuse of a right triangle....
#With the given lengths of the two sides of the right triangle adjacent
#to the right angle.....................

from math import sqrt

print("\nPlease Enter the lengths of the two sides:\n" )

a= float(input("Side a is : "))
b= float(input("Side b is : "))

c= sqrt(a**2 + b**2);

print("\n\nThe length of the hypotenuse is : " , c)
print("\n\nThank you! \n\n")

#end.................................