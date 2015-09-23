# https://www.hackerrank.com/challenges/validate-a-roman-number/

def validateRomanNumeral(roman_numeral):
    import re
    
    return True if re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_numeral) else False

if __name__ == "__main__":
    roman_numeral = input()

    print(validateRomanNumeral(roman_numeral))