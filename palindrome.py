def regularize(possible_palin):
    possible_palin = possible_palin.strip()
    possible_palin = possible_palin.lower()
    possible_palin = possible_palin.replace(' ', '')
    return possible_palin

def match(orig, backwards):
    are_match = (orig == backwards)
    return are_match

def is_palindrome(orig):
    orig = regularize(orig)
    backwards = orig [::-1]         # learned this slicing method from W3Schools article: https://www.w3schools.com/python/python_howto_reverse_string.asp
    return match(orig, backwards)

orig = str(input("Please enter a string: "))
print("Is palindrome: ")
print(is_palindrome(orig))
