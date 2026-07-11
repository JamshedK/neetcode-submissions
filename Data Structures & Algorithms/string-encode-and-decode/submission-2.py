class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        # count how many words and then #12#
        for str in strs: 
            # count how many characters in str
            length = len(str)
            res.append(f"#{length}#{str}")
        print(res)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        # take the encoded string
        idx = 0
        res = []
        while idx < len(s):
            # first character is going to be #, so go to the next
            idx = idx + 1
            count = ''
            while s[idx] != '#':
                count += s[idx]
                idx += 1
            # last character is going to be '#', just increment i
            idx += 1
            # convert count to number
            count = int(count)
            # then get the string until you reach another # or end of line 
            temp = ''
            for j in range(count):
                temp += s[idx]
                idx += 1
            res.append(temp)
        return res