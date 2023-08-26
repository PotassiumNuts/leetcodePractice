class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # define a helper function to perform DFS on the tree
        def dfs(node, max_val):
            # if the node is None, return 0
            if not node:
                return 0
            # initialize a count variable to 0
            count = 0
            # if the node value is greater than or equal to the maximum value found so far,
            # it is a good node, so increment the count and update the maximum value
            if node.val >= max_val:
                count += 1
                max_val = node.val
            # recursively call the dfs function on the left and right children of the node,
            # passing in the updated maximum value, and add the return values to the count
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            # return the count
            return count
        
        # call the dfs function on the root node, passing in negative infinity as the initial maximum value
        return dfs(root, float('-inf'))
    
# create a tree
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print(Solution().goodNodes(root)) # 4