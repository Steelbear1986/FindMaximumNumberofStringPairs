class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        h = 0
        for i in range(len(words)):
            if words[i][::-1] in words[i + 1:]:
                h += 1
        return h

