class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        num_dict = {}

        for i,x in enumerate(nums):
            complement = target - x
            if complement in num_dict.keys():
                return (num_dict[complement], i)
            num_dict[x] = i


if __name__ == "__main__":

    s = Solution()
    nums = [2,7,11,15]
    target = 9

    print(s.twoSum(nums,target))
