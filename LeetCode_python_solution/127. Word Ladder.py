'''Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
题意：单词变换，从begin到end，每次只能变换一个字母，单词只能用一次
思路：bfs，采用bfs通用框架，wordList使用set数据结构，查找需要O(1)，
每次改变word的一个字母，然后判断word是否在wordList中，时间复杂度为O(26*L)，L为单词长度
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList=set(wordList)
        cur_level=[beginWord]
        next_level=[]
        depth=1
        n=len(beginWord)
        while cur_level:
            for item in cur_level:
                if item==endWord:
                    return depth
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        word=item[:i]+c+item[i+1:]
                        if word in wordList:
                            wordList.remove(word)
                            next_level.append(word)
            depth+=1
            cur_level=next_level
            next_level=[]
        return 0