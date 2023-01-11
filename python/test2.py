def leap_year():
    year=int(input("enter year: "))
    if year % 4 == 0:
        print("leap year")
    elif year % 100 != 0:
        print("NOT LEAP")
    elif year % 400 == 0:
        print("leap year")
    else:
        print("pass")

leap_year()

#method 2
def leap_year():
    Year=int(input("enter year: "))
    if ((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):

       print(leap )
    else:
        print( "not leap")

leap_year()        
