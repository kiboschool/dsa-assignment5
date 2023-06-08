from collections import deque
import random

class LinkedBST:
    class BSTNode:
        def __init__(self, key, val, left=None, right=None, parent=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self, root=None):
        self.root = root

    def insert(self, key, val):
        # find the parent of the new node
        parent = None
        trav = self.root
        while trav is not None:
            if trav.key == key:
                # key already exists
                return False

            parent = trav
            if key < trav.key:
                trav = trav.left
            else:
                trav = trav.right

        # insert the new node
        new_node = LinkedBST.BSTNode(key, val)
        if parent is None:
            # tree was empty
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.parent = parent
        return True

    def __search(self, root, key):
        if root is None:
            return None
        elif root.key == key:
            return root.val
        elif root.key > key:
            return self.__search(root.left, key)
        else:
            return self.__search(root.right, key)

    def search(self, key):
        return self.__search(self.root, key)

    def level_order_print(self):
        print("Note: doesn't show links between children or shape of tree; only shows levels of tree")
        if self.root is None:
            return

        q = deque([(self.root, 0)])

        current_depth = 0
        while len(q) > 0:
            node, depth = q.popleft()
            if depth != current_depth:
                print() # go to next level
                current_depth = depth
            print(node.key, end=' ')
            if node.left is not None:
                q.append((node.left, depth + 1))
            if node.right is not None:
                q.append((node.right, depth + 1))
        print()

    def min_key(self):
        if self.root is None:
            return None

        trav = self.root
        while trav.left is not None:
            trav = trav.left
        return trav.key

    def delete_max_key(self):
        trav = self.root
        if self.root is None:
            return None

        if self.root.right is None:
            key = self.root.key
            self.root = self.root.left
            return key

        while trav.right is not None:
            trav = trav.right

        if trav.parent.right == trav:
            trav.parent.right = trav.left
        else:
            trav.parent.left = trav.left

        return trav.key

    def depth(self, key):
        if self.root is None:
            return -1

        trav = self.root
        d = 0
        while trav is not None:
            if trav.key == key:
                return d
            elif key < trav.key:
                trav = trav.left
            else:
                trav = trav.right
            d += 1

        return -1

    def __range_search(self, root, key_min, key_max):
        if root is None:
            return []

        items = []

        self.nodes_visited += 1

        if root.key > key_min:
            items += self.__range_search(root.left, key_min, key_max)

        if root.key >= key_min and root.key <= key_max:
            items.append(root.key)

        if root.key < key_max:
            items += self.__range_search(root.right, key_min, key_max)

        return items

    def range_search(self, key_min, key_max):
        self.nodes_visited = 0
        return self.__range_search(self.root, key_min, key_max)
