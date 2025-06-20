def findMax(numbers):
    if not numbers:
        return None
    
    max_number = numbers[0]
    for num in numbers:
        if num >     max_number:
            max_number = num

    return max_number

print(findMax([1,2,3,5,7,8,9]))