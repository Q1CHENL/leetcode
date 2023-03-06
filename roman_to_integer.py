class RomanToInteger:

    # use map to avoid if statements
    def roman_to_int(self, s: str) -> int:
        # Define the roman to integer conversion dictionary
        roman_to_int_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Reverse the input string
        rd = s[::-1]

        # Initialize the converted value to zero
        converted = 0

        # Initialize a variable to keep track of the previous value
        prev = 0

        # Loop through the reversed string
        for c in rd:
            # Get the value of the current symbol from the dictionary
            if c not in roman_to_int_dict:
                print('Invalid roman numeral!')
                return -1
            curr = roman_to_int_dict[c]

            # If the current value is less than the previous value, subtract it from the converted value
            # because the char value should always get bigger if no 4, 40 etc
            if curr < prev:
                converted -= curr
            # Otherwise, add it to the converted value
            else:
                converted += curr

            # Update the previous value to the current value
            prev = curr

        return converted


r = RomanToInteger()
res = r.roman_to_int('sssss')
print(res)

# My original idea: loop through s, check every char with if
# class Solution:
#     def roman_to_int(self, s: str) -> int:
#         rd = s[::-1]
#         converted = 0
#         for i in range(len(rd)):
#             curr = rd[i]
#             if curr == 'I':
#                 if (i - 1) >= 0 and rd[i - 1] == 'V':
#                     converted -= 1
#                 elif (i - 1) >= 0 and rd[i - 1] == 'X':
#                     converted -= 1
#                 else:
#                     converted += 1
#                 continue
#
#             if curr == 'V':
#                 converted += 5
#                 continue
#
#             if curr == 'X':
#                 if (i - 1) >= 0 and rd[i - 1] == 'L':
#                     converted -= 10
#                 elif (i - 1) >= 0 and rd[i - 1] == 'C':
#                     converted -= 10
#                 else:
#                     converted += 10
#                 continue
#
#             if curr == 'L':
#                 converted += 50
#                 continue
#
#             if curr == 'C':
#                 if (i - 1) >= 0 and rd[i - 1] == 'D':
#                     converted -= 100
#                 elif (i - 1) >= 0 and rd[i - 1] == 'M':
#                     converted -= 100
#                 else:
#                     converted += 100
#                 continue
#
#             if curr == 'D':
#                 converted += 500
#                 continue
#
#             if curr == 'M':
#                 converted += 1000
#
#         return converted
