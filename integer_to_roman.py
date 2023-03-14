class IntegerToRoman:
    # From leetcode, concise solution: 
    # optimized dictionary and
    # divide from biggest possible number
    def int_to_roman(self, num: int) -> str:
        symlst = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]
        res = ""
        for sym, val in reversed(symlst):
            if num//val:
                count = num//val
                res += (sym*count)
                num = num % val

        return res

    # My original idea: loop through every char and
    # append corresponding str: time consuming
    #
    # def inter_to_roman(self, num: int) -> str:
    #     int_to_roman_dict = {
    #         1: 'I',
    #         5: 'V',
    #         10: 'X',
    #         50: 'L',
    #         100: 'C',
    #         500: 'D',
    #         1000: 'M'
    #     }
    #     intstr = str(num)
    #     ln = len(intstr)
    #     roman = ''
    #     for i in range(ln):
    #         if intstr[i] == '9':  # special case
    #             if ln - i == 3:
    #                 roman += 'CM'
    #             elif ln - i == 2:
    #                 roman += 'XC'
    #             elif ln - i == 1:
    #                 roman += 'IX'
    #         elif intstr[i] == '4':  # special case
    #             if ln - i == 3:
    #                 roman += 'CD'
    #             elif ln - i == 2:
    #                 roman += 'XL'
    #             elif ln - i == 1:
    #                 roman += 'IV'
    #         else:
    #             if int(intstr[i]) >= 5:
    #                 roman += int_to_roman_dict[5*(10**(ln-i-1))]
    #                 for j in range(int(intstr[i]) - 5):
    #                     roman += int_to_roman_dict[1*(10**(ln-i-1))]
    #             else:
    #                 for k in range(int(intstr[i])):
    #                     roman += int_to_roman_dict[1*(10**(ln-i-1))]
    #     return roman


itr = IntegerToRoman()
roman = itr.inter_to_roman(58)
print(roman)
