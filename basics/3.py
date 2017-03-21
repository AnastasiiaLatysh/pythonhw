def reverse(word) :
    new_word = ""
    for i in word : new_word = i + new_word
    return new_word

print( reverse("I am testing"))