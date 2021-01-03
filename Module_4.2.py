def palindrome_check(myString):
    """
        Checks if the string is a palindrome, based on entered data
    """
    if myString == myString[::-1]:
        print ("True")
    else:
        print ("False")
palindrome_check('kajak')