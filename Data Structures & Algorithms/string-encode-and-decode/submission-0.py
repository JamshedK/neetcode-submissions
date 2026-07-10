class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            length = len(string)
            res = res + f'#{length}#'
            res += string

        return res

    def decode(self, s: str) -> List[str]:
        i = 1
        res = []
        while i < len(s):
            num = ''
            # count the length of the next string
            while s[i] != '#':
                num += s[i]
                i += 1
            length = int(num)
            # skip the # sign
            i += 1
            # get the word
            word = ''
            for j in range(length):
                word += s[i+j]
            res.append(word)
            # print(word)
            i += length
            i += 1

        return res
            
