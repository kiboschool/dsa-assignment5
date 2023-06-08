import unittest
import io
import sys
from linked_bst import LinkedBST

class TestLinkedBST(unittest.TestCase):
    def setUp(self):
        self.tree = LinkedBST()
        self.tree.insert(6, 19)
        self.tree.insert(3, 7)
        self.tree.insert(9, 8)
        self.tree.insert(1, -10)
        self.tree.insert(2, 20)
        self.tree.insert(8, 15)
        self.tree.insert(10, -5)
        self.tree.insert(12, 0)

    def test_min_key(self):
        assert self.tree.min_key() == 1

    def test_min_key_empty_tree(self):
        tree = LinkedBST()
        assert tree.min_key() == None

    def test_delete_max_key(self):
        assert self.tree.delete_max_key() == 12
        captured = io.StringIO()
        sys.stdout = captured
        self.tree.level_order_print()
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == "Note: doesn't show links between children or shape of tree; only shows levels of tree\n6 \n3 9 \n1 8 10 \n2 \n"

    def test_delete_max_key_empty_tree(self):
        tree = LinkedBST()
        assert tree.delete_max_key() == None

    def test_depth(self):
        assert self.tree.depth(12) == 3

    def test_depth_empty_tree(self):
        tree = LinkedBST()
        assert tree.depth(20) == -1

    def test_range_search(self):
        assert self.tree.range_search(4, 10) == [6, 8, 9, 10]

    def test_range_search_empty_tree(self):
        tree = LinkedBST()
        assert tree.range_search(8, 15) == []

    def test_range_search_efficiency(self):
        tree = LinkedBST()
        tree.insert(8, 'value')
        tree.insert(3, 'value')
        tree.insert(1, 'value')
        tree.insert(5, 'value')
        tree.insert(4, 'value')
        tree.insert(7, 'value')
        tree.insert(9, 'value')
        tree.insert(13, 'value')
        tree.insert(10, 'value')

        tree.range_search(5, 10)
        assert tree.nodes_visited == 7, "range_search() should only visit 7 nodes (see README example)"
