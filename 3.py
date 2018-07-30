class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ll = []
        mxl = 0
        for i in range(len(s)):
            st = ''
            j = i
            while j < len(s) and s[j] not in st:
                st = st + s[j]
                j = j + 1

            mxl = mxl if mxl > len(st) else len(st)
        return mxl

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))
