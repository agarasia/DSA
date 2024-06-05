def romanToInt(s):
    roman_values = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
    
    total = 0
    prev_value = 0

    # Traverse the Roman numeral string from right to left
    for char in reversed(s):
        value = roman_values[char]
        
        # If the current value is less than the previous value, subtract it, otherwise add it
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total
    


roman = "XXIX"   # 1949

print(romanToInt(roman))