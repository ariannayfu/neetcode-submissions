class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        longest = 0
        
        for right, ch in enumerate(s):
            if ch in chars and chars[ch] >= left:
                left = chars[ch] + 1
            chars[ch] = right
            longest = max(longest, right - left + 1)
            
        return longest
        