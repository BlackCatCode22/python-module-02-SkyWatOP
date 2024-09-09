a = float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
big = 0
if a >= b:
    if a >= c:
        # if a is bigger than c then a is the biggest
        big = a
    else:
        # c is biggest since a was bigger than b
        big = c
else:
    if b >= c:
        # b is bigger than c
        big = b
    else:
        # c was bigger than a or b
        big = c

print("The largest is: ", big)



