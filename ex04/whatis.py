import sys

arglen = len(sys.argv)

if arglen > 2:
    print("AssertionError: more than one argument is provided")

elif arglen == 2:
    try:
        res = int(sys.argv[1])
        if res % 2:
            print("I'm Even.")
        elif res == 0:
            print("I'm Zero, kinda Even but not...")
        else:
            print("I'm Odd.")
    except:
        print("AssertionError: argument is not an integer")


    
