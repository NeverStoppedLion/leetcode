class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        map_key = []
        map_key = zip(nums, range(0, length))
        map_key.sort(lambda x, y: x[0] - y[0])
        i = 0
        j = -1
        t = map_key[i][0] + map_key[j][0]
        while (t != target):
            if(t > target) :
                j -= 1
            elif (t < target) :
                i += 1
            t = map_key[i][0] + map_key[j][0]
        res = [map_key[i][1], map_key[j][1]]
        res.sort()
        return res

if __name__ == "__main__":
    nums = [11, 7, 2, 15]
    target = 9
    solution = Solution()
    res = solution.twoSum(nums, target)
    print res
