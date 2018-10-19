'''请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
思路：用一个128的数组来表示每个字符出现的次数（ascii有128个字符），
字符串只保存第一次出现的字符，然后遍历字符串，判断字符串的第一个字符是否只出现了一次
'''


class Solution:
    # 返回对应char
    def __init__(self):
        self.char=[0]*128
        self.string=''
    def FirstAppearingOnce(self):
        # write code here
        for i in self.string: # 判断字符串中那个字符只出现了一次
            if self.char[ord(i)]==1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.char[ord(char)]+=1 # 统计每个字符出现的次数
        if self.char[ord(char)]==1: # 如果这个字符是第一次出现，加入到字符串中
            self.string+=char