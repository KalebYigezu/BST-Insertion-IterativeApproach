class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def insert(root, key):
    temp = Node(key)

    # If tree is empty
    if root is None:
        return temp

    parent = None
    curr = root
    while curr is not None:
        parent = curr
        if curr.key > key:
            curr = curr.left
        elif curr.key < key:
            curr = curr.right
        else:
            return root  # Key already exists
    if parent.key > key:
        parent.left = temp
    else:
        parent.right = temp

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)

