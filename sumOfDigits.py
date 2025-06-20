def sum(input):
    total = 0

    for digit in str(input):
        total += int(digit)
    return total

print(sum(12345))