#617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #if doesn't overlap, NOT null node is used
        if t1 is None: 
            return t2 
        if t2 is None:
            return t1
        t1.val += t2.val                              #if overlap, adds together
        t1.left = self.mergeTrees(t1.left,t2.left)    #adds all the left side
        t1.right = self.mergeTrees(t1.right,t2.right) #adds all the right side
        return t1
