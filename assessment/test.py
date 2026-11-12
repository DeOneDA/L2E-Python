def integer_to_roman(num):
    romans = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
              (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
              (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), 
              (1, "I")]

    result = ""
    index = 0
    while num > 0:
        value, symbol = romans[index]
        if num//value > 0:
            result += symbol
            num -= value
        else:
            index += 1
        
            
    return result


print(integer_to_roman(3999))