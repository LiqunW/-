'''
“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
按照空格拆分字符串，然后倒序合并即可，注意要添加空格
'''
class Solution:
    def ReverseSentence(self, s):
        # write code here
        tmp=s.split(' ')
        return ' '.join(tmp[i] for i in range(len(tmp)-1,-1,-1))