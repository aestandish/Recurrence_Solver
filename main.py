# This program solves a second-order linear homogeneous recurrence relation and outputs its solution
# Addie Standish, 4/24/23

import math  # used to calculate the square root in the quadratic formula


def quadratic_formula(a, b, c):  # calculates the roots of the equation using the quadratic formula and returns a tuple
    output1 = ((-1)*b + math.sqrt(b**2 - 4*a*c))/(2*a)
    output2 = ((-1)*b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return output1, output2


def discriminant(a, b, c):  # calculates the discriminant of the equation
    return b**2 - 4*a*c


answer = 'y'  # answer variable used for looping so the program can be repeated
while answer == 'y':
    print("Enter the coefficients A, B, and C of the recurrence relation in the form A*S(k) + B*S(k-1) + C*S(k-2) = 0:")
    A = float(input("Enter the value of A: "))
    B = float(input("Enter the value of B: "))
    C = float(input("Enter the value of C: "))
    if discriminant(A, B, C) > 0:  # checks to see if the equation has distinct real roots
        x1 = str(quadratic_formula(A, B, C)[0])  # gets the first output of the quadratic formula tuple
        x2 = str(quadratic_formula(A, B, C)[1])  # gets the second output of the quadratic formula tuple
        print("The general solution for the recurrence relation is: S(k) = c₁(" + x1 + ")ᵏ", "+ c₂(" + x2 + ")ᵏ")
    elif discriminant(A, B, C) == 0:  # checks to see if the equation has repeated real roots
        x1 = str(quadratic_formula(A, B, C)[0])  # gets the first output of the quadratic formula tuple
        x2 = str(quadratic_formula(A, B, C)[1])  # gets the second output of the quadratic formula tuple
        print("The general solution for the recurrence relation is: S(k) = c₁(" + x1 + ")ᵏ", "+ c₂k(" + x2 + ")ᵏ")
    else:  # the discriminant is negative and the equation has complex roots
        print("The recurrence relation has complex roots.")
    print("Would you like to solve another recurrence relation? Enter y for yes and anything else for no: ")
    answer = input()












