a=int(input("enter side to triangle"))
b=int(input("enter side to triangle"))
c=int(input("enter side to triangle"))
if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
    print("it is a right angle triangle")
else:
    print("it is not a right angle triangle")

