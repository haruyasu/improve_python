# Trees
# Tree Level Order Pring
class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

import collections
def levelOrderPrint(tree):
    if not tree:
        return

    nodes = collections.deque([tree])
    currentCount = 1
    nextCount = 0

    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1

        print(currentNode.val, end="")

        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1

        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1

        if currentCount == 0:
            print("\n")
            currentCount, nextCount = nextCount, currentCount

root = Node(1)
root.left = Node(2)
root.right = Node(3)
levelOrderPrint(root)


####
# Trim a Binary Search Tree
def trimbst(tree, minVal, maxVal):
    if not tree:
        return

    tree.left = trimbst(tree.left, minVal, maxVal)
    tree.right = trimbst(tree.right, minVal, maxVal)

    if minVal <= tree.val <= maxVal:
        return tree

    if tree.val < minVal:
        return tree.right

    if tree.val > maxVal:
        return tree.left
