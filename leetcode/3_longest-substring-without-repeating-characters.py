"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

import time

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = ''
        words = []
        mx = 0
        for i in range(len(s)):
            found = True if s[i] in word else False
            if not found:
                word += s[i]
            else:
                words.append(word)
                # mx = max(mx, len(word))
                c = i - s[:i:][::-1].find(s[i])
                # print(s[:i:], s[c:i+1])
                word = s[c:i+1]
                # word = s[:i:][::-1][:s[:i:][::-1].rfind(s[i])-1:][::-1]
            # print(f'word : "{word}"  tmp : "{found}"')
        else:
            words.append(word)
        # mx = max(mx, len(word))
        # print(words)
        length = len(max(words, key = len)) if words else 0
        # print(length)
        return length
        # return mx


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]]+1)
                dic[s[i]] = i
            res = max(res, i+1-j)
            # print(i,j,res,dic)
        return res


t = time.time()
for _ in range(1000):
    s = time.time() #.25 #0.19
    a = Solution() #.3
    # a.lengthOfLongestSubstring("dvdf")
    # a.lengthOfLongestSubstring(" ")
    # a.lengthOfLongestSubstring("")
    # a.lengthOfLongestSubstring("pwwkew")
    a.lengthOfLongestSubstring("abcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdasdasvdhasdkjhasdhnbabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdaabcadefHJghjdsdjfhbjasdhyuadhasdakdghjafjdasdasvdhasdkjhasdhnb")

    # (pw, wke, kew)

print(time.time() - t)
