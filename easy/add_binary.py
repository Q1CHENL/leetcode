class AddBinary(object):
    # Other conversion methods:
    # 1. bin(), takes an integer, converts to binary
    # 2. int('ff', 16), int('1010', 2)
    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        flag = 0
        res = ''
        max_len = max(len(a), len(b))
        min_len = min(len(a), len(b))

        if len(a) > len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a
        # append 0s to shorter, can also use a = a.zfill(max_len)    
        zeros = '0' * (max_len - min_len) 
        shorter = zeros + shorter

        for i in range(max_len - 1, -1, -1):
            sum = int(shorter[i]) + int(longer[i]) + flag
            res += str(sum % 2)
            if sum >= 2:
                flag = 1
            else:
                flag = 0
            
        if flag:
            res += '1'

        return res[::-1]

ab = AddBinary()
a = "11"
b = "1"
c = '1010'
d = '1011'
e = '100'
f = '110010'
res = ab.add_binary(e, f)
print(res)
h = '100'
h = h.zfill(5)
print(h)