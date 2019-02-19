class Solution:
    def sortedSquares(self, A):
        A = sorted(list(map(lambda x: x*x, A)))
        return A

if __name__ == "__main__":
    s = Solution()
    x = [-4, -1, 0, 3, 10]

    print(s.sortedSquares(x))
