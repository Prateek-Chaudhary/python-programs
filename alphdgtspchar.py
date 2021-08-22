a = input("Enter a digit, alphabet or special character\n")
if a.isalpha():
    print("It is an alphabet")
elif a.isdigit():
    print("It is a digit")
elif a.isalnum():
    print("It is an alphanumeric")
else:
        print("It ia a special character")
