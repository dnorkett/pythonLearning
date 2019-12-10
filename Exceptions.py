while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError:
        print("Could not convert to a number")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except:
        print("Something went very wrong")
