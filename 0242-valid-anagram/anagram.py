class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# step 1 : removing and trailing white/blank spaces and converting to lower case
        s = s.strip().lower()
        t = t.strip().lower()

# step 2 : sorting and comparing both the strings

        # return sorted(s) == sorted(t)

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True        


