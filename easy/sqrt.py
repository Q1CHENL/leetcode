class Sqrt(object):
    # def my_sqrt(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     i = 0
    #     while (i*i <= x):
    #         i += 1
    #     return i - 1

    # From leetcode: binary search, so smart
    def my_sqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


sqrt = Sqrt()
res = sqrt.my_sqrt(12345667)
print(res)
