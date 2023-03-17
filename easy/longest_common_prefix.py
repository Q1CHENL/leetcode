
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

# A code block starts with a colon (:) and all statements
# in the block must be indented at the same level. The block
# ends when the indentation returns to the previous level.    
    
strs = ["flower","flow","flight"]
lcp = LongestCommonPrefix()
s = lcp.longest_common_prefix(strs)
print(s)