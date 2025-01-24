import hashlib
#### `merkle.py`
class MerkleTree:
    def __init__(self, data):
        self.data = data
        self.tree = self.build_tree()

    def hash(self, value):
        return hashlib.sha256(value.encode()).hexdigest()

    def build_tree(self):
        if not self.data:
            return []

        tree = [self.hash(item) for item in self.data]
        while len(tree) > 1:
            if len(tree) % 2 != 0:
                tree.append(tree[-1])  # Duplicate last item if odd number
            tree = [self.hash(tree[i] + tree[i + 1]) for i in range(0, len(tree), 2)]
        return tree

    def get_root(self):
        return self.tree[0] if self.tree else None