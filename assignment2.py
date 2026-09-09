a=int(input("Enter 1st no"))
b=int(input("Enter 2nd no"))
c=int(input("Enter 3rd no"))
if a>b:
    if a>c:
        print(a,"is the greatest")
    else:
        print(c,"is the greatest")
elif b>c:
    if b>a:
        print(b,"is the greatest")
    else:
         print(a,"is the greatest")
else:
    print(c,"is the greatest")