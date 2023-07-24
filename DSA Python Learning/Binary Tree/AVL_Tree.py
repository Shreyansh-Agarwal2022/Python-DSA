class AVLTree:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return self.Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        balance_factor = self._get_balance_factor(node)
        if balance_factor > 1 and key < node.left.key:
            # Left-Left case
            return self._right_rotate(node)
        if balance_factor > 1 and key > node.left.key:
            # Left-Right case
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance_factor < -1 and key > node.right.key:
            # Right-Right case
            return self._left_rotate(node)
        if balance_factor < -1 and key < node.right.key:
            # Right-Left case
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._find_min_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        if node is None:
            return node
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        balance_factor = self._get_balance_factor(node)
        if balance_factor > 1 and self._get_balance_factor(node.left) >= 0:
            # Left-Left case
            return self._right_rotate(node)
        if balance_factor > 1 and self._get_balance_factor(node.left) < 0:
            # Left-Right case
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance_factor < -1 and self._get_balance_factor(node.right) <= 0:
            # Right-Right case
            return self._left_rotate(node)
        if balance_factor < -1 and self._get_balance_factor(node.right) > 0:
            # Right-Left case
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    def _left_rotate(self, node):
        y = node.right
        t2 = y.left
        y.left = node
        node.right = t2
        node.height = 1 + max(self._get_height(node.left),
                            self._get_height(node.right))
        y.height = 1 + max(self._get_height(y.left),
                        self._get_height(y.right))
        return y
    def _right_rotate(self, node):
        y = node.left
        t2 = y.right
        y.right = node
        node.left = t2
        node.height = 1 + max(self._get_height(node.left),
                            self._get_height(node.right))
        y.height = 1 + max(self._get_height(y.left),
                        self._get_height(y.right))
        return y

