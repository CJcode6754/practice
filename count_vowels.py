def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    return count


userInput = input('Enter letter here: ')
vowelcount = count_vowels(userInput)
print("The number of vowels is: ", vowelcount)    
