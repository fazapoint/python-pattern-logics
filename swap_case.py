def swap_case(s):
    accumulator = ""
    for letter in s:
        if letter.islower():
            accumulator = accumulator + letter.upper()
        elif letter.isupper():
            accumulator = accumulator + letter.lower()
        else:
            accumulator = accumulator + letter
    return accumulator

print(swap_case("faZA #RamADhaNi"))