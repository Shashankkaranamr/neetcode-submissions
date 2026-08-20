class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L=len(beginWord)
        all_words=wordList+[beginWord]
        visited=set(beginWord)
        word_list=defaultdict(list)
        queue=deque()

        for word in all_words:
            for i in range(L):
                pattern=word[:i]+"*"+word[i+1:]
                word_list[pattern].append(word)
        count=1
        queue.append((beginWord,count))

        while queue:
            word,count=queue.popleft()
            if word==endWord:
                return count
            for i in range(L):
                pattern=word[:i]+"*"+word[i+1:]
                for neighbor in word_list[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,count+1))
        return 0
        
        



        