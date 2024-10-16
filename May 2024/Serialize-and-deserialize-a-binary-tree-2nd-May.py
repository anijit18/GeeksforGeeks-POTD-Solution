class Solution:

    def serializeUtil(self, root, a):
        # Base case if node is null.
        if root is None:
            a.append(-1)
            return
        # Storing the data at node in list.
        a.append(root.data)

        # Calling function recursively for left and right subtrees.
        self.serializeUtil(root.left, a)
        self.serializeUtil(root.right, a)

    def serialize(self, root):
        serialized = []
        self.serializeUtil(root, serialized)

        # Returning the list.
        return serialized

    def kewl(self, a, index):
        # Base case if there are no more elements in list.
        if index[0] == len(a) or a[index[0]] == -1:
            index[0] += 1
            return None

        # Creating new node for storing current element.
        root = Node(a[index[0]])
        index[0] += 1

        # Calling function recursively for left and right subtrees.
        root.left = self.kewl(a, index)
        root.right = self.kewl(a, index)
        return root

    def deSerialize(self, a):
        index = [0]
        # Returning the tree.
        return self.kewl(a, index)
