from lca import *
from TreeNode import *
from Graph import *
from lca_dag import *
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

    def test_simple_DAG(self):
        # cannot test DAG support as LCA assumes Binary Tree implemented

        g = Graph(7) # number of vertexes
        g.add_edge(1,0)
        g.add_edge(2,1)
        g.add_edge(4,1)
        g.add_edge(3,2)
        g.add_edge(5,4)
        g.add_edge(6,3)
        g.add_edge(6,5)

        t = LCA_DAG()
        self.assertEqual(t.lowestCommonAncestor(g, 3, 5), [1])
        self.assertEqual(t.lowestCommonAncestor(g, 2, 4), [1])
        self.assertEqual(t.lowestCommonAncestor(g, 0, 4), [0])
        self.assertEqual(t.lowestCommonAncestor(g, 3, 6), [3])

    def test_multiple_solutions_DAG(self):
        g = Graph(6)
        g.add_edge(2,0)
        g.add_edge(1,0)
        g.add_edge(3,2)
        g.add_edge(5,2)
        g.add_edge(5,1)
        g.add_edge(4,1)
        g.add_edge(4,3)
        t = LCA_DAG()

        self.assertEqual(t.lowestCommonAncestor(g, 4, 5), [1,2])
        self.assertEqual(t.lowestCommonAncestor(g, 2, 1), [0])
        self.assertEqual(t.lowestCommonAncestor(g, 1, 2), [0])
        self.assertEqual(t.lowestCommonAncestor(g, 3, 4), [3])

    def test_no_solution_DAG(self):
        g = Graph(6)
        g.add_edge(2,0)
        g.add_edge(3,4)
        t = LCA_DAG()

        self.assertEqual(t.lowestCommonAncestor(g, 3, 2), [])
        self.assertEqual(t.lowestCommonAncestor(g, 4, 2), [])

if __name__ == '__main__':
    unittest.main()
