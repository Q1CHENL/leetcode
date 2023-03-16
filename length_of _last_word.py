class LengthOfLastWord:
    def length_of_last_word(self, s: str) -> int:
        length = 0
        met = False
        for c in reversed(s):
            if c == ' ':
                if met == False:
                    continue
                else:
                    break
            else:
                length += 1
                met = True
                
        return length

lolw = LengthOfLastWord()
s = "   fly me   to   the moon  "
s2 = "luffy is still joyboy"
length = lolw.length_of_last_word(s2)
print(length)

# or use python built-in split and strip
                