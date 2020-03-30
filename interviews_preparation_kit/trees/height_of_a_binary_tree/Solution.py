class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    return max(subtree_height(root.left), subtree_height(root.right))


def subtree_height(root):
    if root is None:
        return 0

    left_height = 1
    right_height = 1

    if root.left is not None:
        left_height += subtree_height(root.left)
    if root.right is not None:
        right_height += subtree_height(root.right)

    return max(left_height, right_height)


f = open("data.txt", "r")

tree = BinarySearchTree()
t = int(f.readline().strip())

arr = list(map(int, f.readline().strip().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
