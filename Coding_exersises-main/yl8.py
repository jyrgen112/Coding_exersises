a = int(input("enter a year: "))
if (a % 400)  == 0 or (a % 4):
    print("leap year")
else:
    print("over year")