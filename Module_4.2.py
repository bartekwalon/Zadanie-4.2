import string
def palindrome(str):
    """
        Checks if the string is a palindrome, based on entered data
    """
    alphabet=string.ascii_lowercase
    temp=""
    for c in str.lower():
        if c in alphabet:
            temp+=c
    return temp==temp[::-1]
print(palindrome('Może jutro ta dama sama da tortu jeżom.'))