#general tree which can have any number/letter of elements  
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        #leftsearchtree
        self.left = None #elements are less than the current node
        #rightsearchtree
        self.right = None #elements are greater than the current node