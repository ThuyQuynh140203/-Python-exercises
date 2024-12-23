def is_valid_cccd(cccd):
    if len(cccd) != 12 or not cccd.isdigit():
        return False
    total_sum = 0
    for i, digit in enumerate(cccd):
        digit = int(digit)
        if i % 2 == 0:  # If the position is even (including 0)
            total_sum += digit
        else:  # If the position is odd
            doubled = digit * 2
            if doubled > 9:
                doubled = doubled - 9  # Sum the digits of the result
            total_sum += doubled
    return total_sum % 10 == 0

# Test cases
print(is_valid_cccd("079230000009"))
print(is_valid_cccd("079230000001"))