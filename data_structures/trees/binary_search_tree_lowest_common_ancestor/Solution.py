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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    if root.info == v1 or root.info == v2:
        return root

    left = find(root.left, v1, v2)
    right = find(root.right, v1, v2)

    if left[0] is not None and left[1] is not None:
        return left[0]

    if right[0] is not None and right[1] is not None:
        return right[0]

    return root


def find(root, v1, v2):
    if root is None:
        return None, None
    left = find(root.left, v1, v2)
    right = find(root.right, v1, v2)

    if left[0] is not None and left[1] is not None:
        return left
    if right[0] is not None and right[1] is not None:
        return right

    if left[0] is not None and right[1] is not None:
        return root, root
    if right[0] is not None and left[1] is not None:
        return root, root
    if root.info == v1 and right[1] is not None:
        return root, root
    if root.info == v1 and left[1] is not None:
        return root, root
    if root.info == v2 and right[0] is not None:
        return root, root
    if root.info == v2 and left[0] is not None:
        return root, root

    if root.info == v1:
        return root, None
    if root.info == v2:
        return None, root

    if left[0] is not None or left[1] is not None:
        return left
    if right[0] is not None or right[1] is not None:
        return right

    return None, None


f = open("data.txt", "r")

tree = BinarySearchTree()
t = int(f.readline())

arr = list(map(int, f.readline().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, f.readline().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
