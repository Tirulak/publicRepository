roman_numbers_dict = {
                    1000: 'M',
                    500: 'D',
                    400: 'CD',
                    100: 'C',
                    90: 'XC',
                    50: 'L',
                    40: 'XL',
                    10: 'X',
                    9: 'IX',
                    5: 'V',
                    4: 'IV',
                    1: 'I'
                    }

sorted_keys = sorted(roman_numbers_dict.keys(), reverse=True)

try:
    def convert_arabic_to_roman(arabic_number):

        roman_number = ''
        for key in sorted_keys:
            while arabic_number >= key:
                roman_number += roman_numbers_dict[key]
                arabic_number -= key
        return roman_number


    number = int(input('Please enter an arabic number :)  '))
    print(convert_arabic_to_roman(number))
except ValueError:
    print('Please enter only arabic numbers, with no planes, two towers or bombs')
