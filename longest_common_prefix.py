
class LongestCommonPrefix:
    # use fisrt element as iterator
    def longest_common_prefix(self, strs: list[str]) -> str:
        end = 0
        for i in range(len(strs[0])):
            curr = (strs[0])[i]
            for j in range(len(strs)):
                if i < len(strs[j]) and (strs[j])[i] == curr:
                    continue
                else : 
                    return (strs[0])[0:end]
            end += 1   
        return  strs[0]
    

strs = ["dog","racecar","car"]
lcp = LongestCommonPrefix()
s = lcp.longest_common_prefix(strs)
print(s)