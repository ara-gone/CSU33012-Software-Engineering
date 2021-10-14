from lca import *
from TreeNode import *
import unittest

class MyTest(unittest.TestCase):

    def test_empty(self):
        p = TreeNode(5)
        q = TreeNode(3)

        t = LCA()
        t.add(None, 3)

        self.assertEqual(t.lowestCommonAncestor(None, p, q),None)

    def test_balanced(self):
        p = TreeNode(5)
        q = TreeNode(3)

        t = LCA()
        t.add(p, 3)

        self.assertEqual(t.lowestCommonAncestor(p, p, q).val,p.val)
        self.assertEqual(t.lowestCommonAncestor(p, q, p).val,p.val)

    def test_perfect(self):
        p = TreeNode(11)
        q = TreeNode(18)

        t = LCA()
        root = TreeNode(10)
        t.add(root,6)
        t.add(root,14)
        t.add(root,5)
        t.add(root,8)
        t.add(root,11)
        t.add(root,18)

        self.assertEqual(t.lowestCommonAncestor(root, p, q).val,14)

        p = TreeNode(5)
        q = TreeNode(8)

        self.assertEqual(t.lowestCommonAncestor(root, p, q).val,6)

        p = TreeNode(6)
        q = TreeNode(14)

        self.assertEqual(t.lowestCommonAncestor(root, p, q).val,10)

        p = TreeNode(6)
        q = TreeNode(18)

        self.assertEqual(t.lowestCommonAncestor(root, p, q).val,10)

        p = TreeNode(14)
        q = TreeNode(18)

        self.assertEqual(t.lowestCommonAncestor(root, p, q).val,14)

if __name__ == '__main__':
    unittest.main()
