# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        preorder_left_node_amount = inorder_root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : preorder_left_node_amount + 1], inorder[ : inorder_root_index])
        root.right = self.buildTree(preorder[preorder_left_node_amount + 1 : ], inorder[inorder_root_index + 1 : ])
        
        return root
        
        
