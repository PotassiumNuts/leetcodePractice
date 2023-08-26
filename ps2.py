# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        def dfs (node,ls, res):
            if not node:
                return
            ls.append(node.val)


            if node.left == None and node.right == None:
                if sum(ls) == targetSum:
                    res.append(ls[:])
            dfs(node.left,ls,res)
            dfs(node.right,ls,res)
            ls.pop()

            return ls
        res = []
        dfs(root, [], res)

        return res
    
# create a tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(Solution().pathSum(root, 22)) # [[5,4,11,2],[5,8,4,5]]

        