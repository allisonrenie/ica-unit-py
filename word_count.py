def count_words(sentence):
    words = 0
    for x in sentence:
        if x == " ":
            words += 1
    words += 1
    return words

sentence = str(input("Please enter a sentence: "))
words = count_words(sentence)
print("Your sentence has " + words + "words.")
