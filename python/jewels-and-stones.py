class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        jewels = [x for x in J]
        total = sum(list(map(lambda x: S.count(x), jewels)))

        return total
