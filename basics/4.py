def is_palindrome(word) :
    if str(word) == str(word[::-1])  :
        return True
    else :
        return False


print( is_palindrome("abbba"))
print( is_palindrome("abba"))
print( is_palindrome("hello"))