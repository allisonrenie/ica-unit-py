def regularize(possible_palin):
    strip(possible_palin)
    lower(possible_palin)
    possible_palin.replace(" ", "")

def match(orig, backwards):
    are_match = (orig == backwards)
    return are_match

orig = str(input("Please enter a string: "))
regularize(orig)
backwards = orig [::-1]

print("Is palindrome: ")
print(match(orig, backwards))