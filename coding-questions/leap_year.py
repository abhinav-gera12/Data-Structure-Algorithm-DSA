'''
(Q) - Determine if year is a leap year or not using nested condition statements
'''

year = int(input("Enter the year: "))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year")
