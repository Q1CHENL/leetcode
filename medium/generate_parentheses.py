class GenerateParentheses(object):

    # My method: passed but extremly slow
    # def is_valid(self, s):
    #     depth = 0
    #     for c in s:
    #         if c == '(':
    #             depth += 1
    #         else:
    #             depth -= 1
    #         if depth < 0:
    #             return False
    #     return True if depth == 0 else False

    # def generate_parentheses(self, n):
    #     if n == 0:
    #         return []
    #     if n == 1:
    #         return ['()']
    #     root = '('
    #     total = []

    #     def impl(root, n):
    #         if n == 0:
    #             return
    #         left = root + '('
    #         right = root + ')'
    #         total.append(left)
    #         total.append(right)
    #         impl(left, n-1)
    #         impl(right, n-1)
    #     impl(root, n * 2)
    #     for t in total.copy():
    #         if (not self.is_valid(t) or len(t) != n*2):
    #             total.remove(t)
    #     return total

    # This does not generates the parenthesis in the required order
    #  def generate_parentheses(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     if n == 0:
    #         return []
    #     if n == 1:
    #         return ['()']
    #     plist = ['()']
    #     for i in range(n - 1):
    #         tmp = []
    #         for p in plist:
    #             tmp.append('(' + p + ')')
    #         for p in plist:
    #             tmp.append(p + '()')
    #         sep = tmp.pop()
    #         for p in plist:
    #             tmp.append('()' + p)
    #         plist = tmp
    #     return plist


p = GenerateParentheses().generate_parentheses(3)
print(p)
# #1, 2, 5,
# ()

# (()), ()()

# ((())), (()()), ()(()), (())(), ()()()

# (((()))), ((()())), (()(())), ((())()), ()(()()()), ()((())),
# ()(()()), ()()(()), ()(())(), ()()()()
