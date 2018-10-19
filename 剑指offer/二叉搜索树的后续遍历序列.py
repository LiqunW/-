'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
思路：二叉树后序遍历的最后一个值是根节点，左子树所有的值都比根节点小，右子树所有的值都比根节点大，以此分割左右子树，然后递归判断
左右子树是否也为后续遍历并且满足bst的性质
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence)==1:
            return True
        root=sequence[-1]
        L_idx=0
        while sequence[L_idx]<root and L_idx<len(sequence)-1:
            L_idx+=1
        R_idx=L_idx
        while R_idx<len(sequence)-1:
            if sequence[R_idx]<root:
                return False
            else:
                R_idx+=1
        left,right=True,True
        if len(sequence[:L_idx])>0:
            left=self.VerifySquenceOfBST(sequence[:L_idx])
        if len(sequence[L_idx:-1])>0:
            right=self.VerifySquenceOfBST(sequence[L_idx:-1])
        return left and right