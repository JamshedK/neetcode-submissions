class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched = set()

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            if a == target[0]:
                matched.add(0)
            if b == target[1]:
                matched.add(1)
            if c == target[2]:
                matched.add(2)

        return len(matched) == 3

        