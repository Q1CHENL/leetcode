# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent. Return the answer in any order.

# telephone-keymapping.png

# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.

class LetterCombination(object):
    # iterative
    # alternative: recursion with inner function
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) <= 0:
            return ""
        mapping = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        mapped = []
        for d in digits:
            mapped.append(mapping[int(d)])
        result = mapped[0].copy()
        for i in range(len(mapped)-1):
            tmp = []
            for d1 in result:
                for d2 in mapped[i+1]:
                    tmp.append(d1+d2)
            result = tmp
        return result


digits = "234"
res = LetterCombination().letter_combinations(digits)
print(res)
