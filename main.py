class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.num = num
        # create an empty list to hold the roman numerals
        generated_numerals = []
        # pull the correct numerals from the list until the input number reaches zero
        while num > 0:
            for rom_val in range(0, len(roman_numeral_values)):
                if roman_numeral_values[rom_val - 1] <= num < roman_numeral_values[rom_val + 1]:
                    generated_numerals.append(roman_numerals[rom_val])
                    num -= roman_numeral_values[rom_val]

        print(''.join(generated_numerals))


# values separate from numerals for list comprehension, since ordering is not supported in dictionaries
roman_numeral_values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000]

# roman numerals at corresponding index values to the roman numeral value list
roman_numerals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'LC', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM',
                  'M', 'MM', 'MMM', 'MMMM']

# ask the user to enter their number
number_input = int(input("Enter the number you want to convert to Roman Numerals: \n"))

number_to_roman = Solution()
number_to_roman.intToRoman(number_input)