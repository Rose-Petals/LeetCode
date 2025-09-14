#Solution One
'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        seen = []
        tempLength = 0
        for char in s:
            while char in seen:
                seen.pop(0)
                tempLength -=1
            tempLength += 1
            seen.append(char)
            if tempLength > length:
                length = tempLength

        return length
'''
#Solution Two
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsInSeen = set()
        length = 0
        seen = deque()
        tempLength = 0

        for char in s:
            while char in charsInSeen:
                charsInSeen.remove(seen.popleft())
                tempLength -=1
            tempLength += 1
            seen.append(char)
            charsInSeen.add(char)
            if tempLength > length:
                length = tempLength

        return length

        #O(n)
        #O(n)
