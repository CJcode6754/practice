def isPalidrome(text):
    # reversed_text = text[::-1]
    # return text == reversed_text
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == text[::-1]

print(isPalidrome('racecar'))
print(isPalidrome('car'))