# Test Script

# Quadratic equation: 
# -b + sqrt(b^2 -4ac) / 2a
# -b - sqrt(b^2 -4ac) / 2a

# Example Of Quadratic Equations With No Real Solution
# x2 + x + 1 = 0

# Example Of Quadratic Equations With 1 real solution
#x^2 - 3x + 2 = 0

# Example Of Quadratic Equations With 2 solutions
# 4x2 + 26x + 12 = 0
# 1x2 + 3/2x - 5/2 

import math

def main():

    a = input('Enter a: ') 
    b = input('Enter b: ')  
    c = input('Enter c: ')

    # check if a fraction or float was inputed
    a = checkInput(a)
    b = checkInput(b)
    c = checkInput(c)

    # run quadratic equation solver
    solve(a, b, c)

    again = input("Solve another equation? Enter y to confirm or any key to quit ")

    if (again == 'y' or again == 'Y' ):

        print("Okay, here we go again:")
        main()

    else:

        print("Goodbye")

def checkInput(variable):

    if ('/' in variable):

        split = variable.split('/')
        numerator = float(split[0])
        denumerator = float(split[1])

        return numerator/denumerator

    else:
    
        return float(variable)

def solve(a, b, c):

    # calculate the discriminant
    # b^2 – 4ac
    d = (b**2) - (4*a*c)
    print("The discriminant is: {0}".format(d) )

    if (d < 0):
    
        print("This equation has no (real) solution.")

    elif (d == 0):

        sol1 = (-b-math.sqrt(d))/(2*a)
        print("This equation has only one (real) solution: {0}".format(sol1))

    else:
    
        sol1 = (-b-math.sqrt(d))/(2*a) 
        sol2 = (-b+math.sqrt(d))/(2*a)  
        print('The solutions are {0} and {1}'.format(sol1,sol2)) 

print('Hi!')
print('This script solves quadratic equations which are in the form: ax^2 + bx + c = 0')
print('Please input whole numbers (e.g. 1), decimals (e.g. 1.5) or fractions (e.g. 2/3 or -3/4)')
print('Never input brackets or letters')

main()