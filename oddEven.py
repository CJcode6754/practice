def oddEven(num):
    result = ''
    if num%2 == 0:
        result = "Even"
    else:
        result = "Odd"

    return result
print(oddEven(8))