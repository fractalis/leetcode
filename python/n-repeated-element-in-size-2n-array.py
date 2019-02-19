from collections import defaultdict

class Solution:
    def repeatedNTimes(self, A):
        counter = defaultdict(lambda: 0)
        for x in A:
            counter[x] += 1
            if counter[x] > 1:
                return x


if __name__ == "__main__":
    s = Solution()
    x = [1,2,3,3]
    y = [2,1,2,5,3,2]
    z = [5,1,5,2,5,3,5,4]

    print(s.repeatedNTimes(x))
    print(s.repeatedNTimes(y))
    print(s.repeatedNTimes(z))
