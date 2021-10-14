from TreeNode import *

class LCA:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                                q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)

    def add(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self.add(node.left, val)
        if val > node.val:
            node.right = self.add(node.right, val)
        return node

    def helper(self, node, p, q):
        if node is None:
            return None

        if node.val == p.val or node.val == q.val:
            return node

        left_subtree = self.helper(node.left, p, q) 	# get left node
        right_subtree = self.helper(node.right, p, q)   # get right node

        if left_subtree is None:
            return right_subtree

        if right_subtree is None:
            return left_subtree

        return node

#if __name__ == '__main__':
#    aNode1 = TreeNode(5)
