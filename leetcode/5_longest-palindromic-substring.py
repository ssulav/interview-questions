"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

import timeit

class mySolution:
    def longestPalindrome(self, s: str) -> str:
        print(s)
        p = []
        for i in range(len(s)):
            for j in range(1, i+1):
                temp = s[j:i+1]
                if temp == temp[::-1]:
                    p.append(temp)
        print(p)
        return max(p, key=len)


class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res

    def helper(self, s, l, r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


a = Solution()
s = "xfsxwjqovpvchyjzdqphjsligzljscmzmjzelmbfnqpukbninfbbljouesngmbdyzhqysroeyagglkgorllkrcditzisqhihmithgjcpilkgfdxxqqjpqnoavgkjhojrldsyucfgtzimdbjehrxxqlpaqdddzismsodvternodzxusuehllpujmjjukrilrubbwzdjxbpmvmmwzbrxcxsjsqljjezgyzmsjpucghjxksdfyucpbvwloyhwevzgudhpspgtvsbjqlzmpequxthdonvbmjpeirttllvmtonqmbqxqtdkgichbfzkbhmhotqpkaeshhecshqjvdwgwkegmujwcnmseicesxddrvutxomsgjeylpqiuyezdccarsiprmoqgyifidxhufocfdrbnqczhtztutspaftwctsmynozhakqgvfsvoffyslhoaptkcktopabrxxwrcbyfftleaotwpoqvjjdzxwwqxjnyszjqwjsghkzpvirwnwgsofkjluyxzgboxybzhnmqhkwgltwdjgnemaaadvflrzdqmjufwyuwzoimnvhlxhxjywbopresdrepulsaaexdeddyzeosqfwlnovfpxothrcxhxnumnymofkkuxvclwvuhcelieengfbhvinckrpbjuuewnwvnrvimgmpsfdlcffpdfwmydgzdvluaejwalueygvvojfovuxwhlwojldfpieqqpoqfxhbkcnrtzrnbaagonnawwaqdzamhnvwdtoxlkexihvrqwwimjn"
print(a.longestPalindrome(s))
# t = timeit.Timer(a.longestPalindrome(s))
# print(t.timeit(5))

