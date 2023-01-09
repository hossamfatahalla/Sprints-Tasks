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
