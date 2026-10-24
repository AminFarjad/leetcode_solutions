class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # if endWord not in wordList:
        #     return 0
        


        # hot   0 1 0 1 0 0
        # dot   1 0 1 1 0 0
        # dog   0 1 0 0 1 1
        # lot   1 1 0 0 1 0
        # log   0 0 1 1 0 1
        # cog   0 0 1 0 1 0

        from collections import deque

# def ladderLength(beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + c + word[i+1:]
                    if nxt in words and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
        return 0
        
