from chapter9 import mirroring
def is_palindrome(a_string):
    if a_string in mirroring.reverse(a_string):
        return True
    else:
        return False
print(is_palindrome("abba"))
print(is_palindrome("abbas"))