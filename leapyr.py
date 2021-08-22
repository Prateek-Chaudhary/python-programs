yr = int(input("Enter the year\n"))
if yr % 4 == 0:
    if yr % 100 == 0:
        if yr % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
