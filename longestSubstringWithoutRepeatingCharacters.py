class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        length = len(s)
        m = []
        if length > 0:
            m.append(1)
            max_length = 1
            for i in range(1, length):
                m.append(1)
                for j in range(0, m[i - 1]):
                    if (s[i] != s[i - j - 1]):
                        m[i] += 1
                    else:
                        break
                if (max_length < m[i]):
                    max_length = m[i]

        print m
        return max_length

if (__name__ == "__main__"):
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ckilbkd"))
        
        
