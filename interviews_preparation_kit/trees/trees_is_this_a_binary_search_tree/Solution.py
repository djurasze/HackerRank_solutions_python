class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def checkBST(root):
    return checkBSTRec(root, None, None)


def checkBSTRec(root, upper_limit, lower_limit):
    if root is None:
        return True

    if upper_limit is not None and root.data >= upper_limit:
        return False

    if lower_limit is not None and root.data <= lower_limit:
        return False

    return checkBSTRec(root.left, root.data, lower_limit) and checkBSTRec(root.right, upper_limit, root.data)


f = open("data.txt", "r")

tree = BinarySearchTree()
t = int(f.readline().strip())

arr = list(map(int, f.readline().strip().split()))

for i in range(t):
    tree.create(arr[i])

print(checkBST(tree.root))
