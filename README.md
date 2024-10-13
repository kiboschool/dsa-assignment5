# BST Functions

In this assignment, you will practice manipulating memory and references by implementing BST functions. You will practice working with trees and implementing tree-manipulation functions efficiently.

For background information on writing tree algorithms (both for regular trees and search trees), refer back to the lessons and live classes.

## Starter Code

You are given the file `linked_bst.py`, which includes the implementation of a `LinkedBST` class, which represents a binary search tree.

To begin, `linked_bst.py` contains the following code:

* The definition of a `BSTNode` nested class. Each node in the tree has both a key (`key`) and a value (`val`), as well as `left` and `right` child pointers and a `parent` pointer.
* A constructor (`__init__`) that creates a `LinkedBST` object.
* An `insert()` method that inserts a new (key, value) pair into the tree, maintaining search-tree ordering.
* A `search()` method that searches the tree for a given key and returns the associated value, if any.
* A `level_order_print()` method that prints an *approximation* of the tree, with keys displayed in level order. It only shows the approximate shape of the tree, but doesn't show the links between the nodes. Displaying the tree may be helpful for debugging purposes.

Finally, `linked_bst.py` contains stub implementations of four methods: `min_key()`, `delete_max_key()`, `depth()`, and `range_search()`. Your four main tasks are to implement these methods, as described below.

## Steps to Complete

Implement the following four methods.

1. `min_key()`

    The `min_key()` method should find and return the minimum key in the BST.

    Notes:

    * You should try to implement this method as efficiently as possible. It should not visit any nodes that are not necessary to find the minimum key.
    * If the tree is empty, the method should return `None`.
    * You can write this method using either iteration or recursion.

2. `delete_max_key()`

    The `delete_max_key()` method find the node with the maximum key and delete it from the tree.

    Notes:

    * You should try to implement this method as efficiently as possible. It should not visit any nodes that are not necessary to find and delete the node with the maximum key.
    * You may find it helpful to review the lesson about deleting a node from the lessons. In particular, be careful to handle any children that the largest node may have.
    * If the root node has the maximum key in the tree, be sure to update `self.root`.
    * The method should return the key that was deleted from the tree. If the tree was empty when the method was called, it should return `None`.
    * You can write this method using either iteration or recursion.

3. `depth(key)` (using iteration)

    The `depth()` method should find the depth of the given key and return it. If the key does not exist in the tree, the method should return -1.

    Notes:

    * You should try to implement this method as efficiently as possible. It should not visit any nodes that are not necessary to find the depth of the node with the given key.
    * For full credit, this method must be implemented using iteration.
    * Remember that by definition, the depth of the root node is 0.

4. `range_search(min_key, max_key)`

    The `range_search()` method should perform a *range search* over the tree, returning a list of all keys that are in the range [`min_key`, `max_key`] (inclusive on each side).

    For example, consider the tree below:

    <center>
    <img src="/images/binary-search-tree.png"
         alt="A binary search tree. The root node is 8. Its left and right children are 3 and 9, respectively. The 3 node's left and right children are 1 and 5, respectively. The 5 node's left and right children are 4 and 7, respectively. The 9 node's right child is 13. The 13 node's left child is 10."
    style="width:350px;" />
    </center>

    `range_search(5, 10)` should return `[5, 7, 8, 9, 10]`, since all of those keys are in the range [5, 10].

    * Because this method will require visiting multiple paths, we recommend implementing it using recursion. We have given you the skeleton code for the method, but it's up to you to implement the recursive helper function `__range_search()`.
    * For full credit, you should implement this method as efficiently as possible. It should not visit any nodes (or subtrees) that could not possibly contain keys that are in the range. In the example above, the 1 node and the 4 node would not be visited. Note that even though the 13 node is outside of the requested range, it *did* need to be visited in order to find the 10 node.
    * To test the efficiency of your method, there is a instance variable `self.nodes_visited` in the `LinkedTree` class. Your `__range_search()` method should increment this variable once for every node that is visited in the traversal. There is a unit test to check whether the number of visited nodes is correct.
    * The keys in the range should be returned in the list in sorted order. However, you should *not* explicitly sort the list to achieve this. Instead, you should take advantage of the search-tree ordering to visit the nodes in sorted order.
        * *Hint*: one of the traversal algorithms (pre-order, post-order, or in-order) that we looked at will visit the keys of a binary *search* tree in sorted order.
    * If the tree is empty or if no keys are in the given range, the empty list should be returned.

## Testing

In `test_linked_bst.py`, there are unit tests for each of the four methods described above. Each of the unit tests evaluates a method independently -- regardless of whether you have implemented the other methods in the assignment.

When you upload your submission to Gradescope, you will see the results for some tests, but there may be other edge cases we test during grading that you are not able to see when you submit. So be sure to test thoroughly!
