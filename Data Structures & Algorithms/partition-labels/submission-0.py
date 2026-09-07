from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        counter = Counter(s)

        # print(counter)
        res = []
        while l < len(s):
            r = l
            # print(f'Currently processing {s[l]} at index {l}')
            # add curr l to the temporary set 
            ch = s[r]
            temp_set = set([ch])
            # decrement from counter 
            counter[ch] -= 1
            # if counter is 0, remove from temp_set 
            if counter[ch] == 0:
                temp_set.remove(ch)
                r += 1
            else:
                # otherwise, we gotta keep building
                r += 1
                while r < len(s) and temp_set:
                    # add to set
                    ch = s[r]
                    temp_set.add(ch)
                    counter[ch] -= 1
                    if counter[ch] == 0:
                        temp_set.remove(ch)
                    r += 1
            res.append(r - l)
            l = r 

        return res
