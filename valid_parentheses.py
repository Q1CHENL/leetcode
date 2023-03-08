class ValidParentheses:
    def is_valid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        right_to_left = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for c in s:
            if c in right_to_left.values():
                stack.append(c)
            else:
                if len(stack) == 0 or right_to_left[c] != stack.pop():
                    return False
        if len(stack):
            return False
        return True


valid_parentheses = ValidParentheses()
s1 = '()[]{}'
s2 = '[(){()}[]]'
s3 = '[[[]'
validity = valid_parentheses.is_valid(s3)
print(f'valid: {validity}')
