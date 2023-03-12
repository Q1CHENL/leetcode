class FirstOccurenceInString:
    # My optimized solution, compare substr
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)  # length needle
        if ln > len(haystack):
            return -1
        for i in range(len(haystack) - ln + 1):
            if haystack[i] == needle[0] and haystack[i:i+ln] == needle:
                return i
        return -1
    
    # My original solution, compare each char which is slow
    # def strStr(self, haystack: str, needle: str) -> int:
    #     ln = len(needle) # length needle
    #     if ln > len(haystack): return -1
    #     found = True
    #     index = -1
    #     for i in range(len(haystack) - ln + 1):
    #         index = i
    #         for j in range(ln):
    #             if haystack[i] != needle[j]:
    #                 found = False
    #                 index = -1
    #                 break
    #             found = True
    #             i+=1
    #         if found: return index
    #     return index


f = FirstOccurenceInString()
haystack = 'hello'
needle = 'll'
index = f.strStr(haystack, needle)
print(index)
