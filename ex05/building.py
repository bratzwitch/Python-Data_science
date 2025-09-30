import sys


def main():
    arglen = len(sys.argv)

    if arglen > 2:
        print("AssertionError: more than one argument is provided")

    elif arglen == 1 or arglen == 2:
        if arglen == 1:
            print("What is the text to count?")
            try:
                str = input()
                if str == "":
                    while str == "":
                        print("excuse me?")
                        str = input()
                strlen = len(str)
            except (AssertionError):
                print("\nCtrl+D or Ctrl+C pressed")
                return
        else:
            str = sys.argv[1]
            strlen = len(sys.argv[1])
        i = 0
        upperLet = 0
        lowerLet = 0
        punctMarks = 0
        spaces = 0
        digits = 0
        while strlen > 0:
            try:
                int(str[i])
                digits += 1
            except (AssertionError):
                if str[i].isupper():
                    upperLet += 1
                elif str[i].islower():
                    lowerLet += 1
                elif str[i].isspace():
                    spaces += 1
                else:
                    punctMarks += 1
            i += 1
            strlen -= 1
        print("Upper-case letters:", upperLet)
        print("Lower-case letters:", lowerLet)
        print("Punctuation marks:", punctMarks)
        print("Spaces:", spaces)
        print("Digits:", digits)


if __name__ == "__main__":
    main()
