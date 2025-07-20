def reverse_words(words):
    accumulator = ""
    for x in words:
        accumulator = x + accumulator
    return accumulator

print(reverse_words("dog"))