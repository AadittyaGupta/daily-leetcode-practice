class Solution:
    def makeFancyString(self, s: str) -> str:
        # letter_count = {}
        # result = []

        # for letter in s:
        #     # Count occurrences of each letter
        #     if letter in letter_count:
        #         letter_count[letter] += 1
        #     else:
        #         letter_count[letter] = 1

        #     # Add letter to result only if it appears <= 2 times
        #     if letter_count[letter] <= 2:
        #         result.append(letter)

        # return ''.join(result)

        result = []
        for letter in s:
            if len(result) >= 2 and result[-1] == letter and result[-2] == letter:
                continue
            result.append(letter)
        return ''.join(result)