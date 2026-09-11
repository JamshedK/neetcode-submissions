class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        one = False
        two = False
        three = False
        for i in range(len(triplets)):
            a, b, c = triplets[i]
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                # print(f"one found {triplets[i]}")
                one = True
            if b == target[1]:
                # print(f"two found {triplets[i]}")
                two = True
            if c == target[2]:
                # print(f"three found {triplets[i]}")
                three = True
        
        return one and two and three

        