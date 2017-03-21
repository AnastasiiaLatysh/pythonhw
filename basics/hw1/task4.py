# 4. Define a function `is_palindrome()` that recognizes palindromes (i.e. words that look the same written backwards).
# For example, `is_palindrome("radar")` should return True.

from basics.hw1.task3 import reverse
def is_palindrome(text):
    return text==reverse(text)

#print(is_palindrome('radar'))