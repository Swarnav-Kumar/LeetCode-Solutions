class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        l = list(s)
        while l[-1] == ' ':
            l.pop()
        for i in range(len(l)-1, -1, -1):
            if l[i] == ' ':
                return count
            count += 1
        return count
