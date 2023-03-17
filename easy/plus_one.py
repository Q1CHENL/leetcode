class PlusOne:
    def plus_one(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                continue
            break
        if i == 0 and digits[0] == 0:
            digits.insert(0, 1)
        return digits


po = PlusOne()
digits = [4, 3, 2, 1]
digits2 = [0]
res = po.plus_one(digits2)
print(res)
