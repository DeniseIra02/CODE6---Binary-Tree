#general tree which node can have any of the elements  
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        #leftsearchtree
        self.left = None #elements are less than the current node
        #rightsearchtree
        self.right = None #elements are greater than the current node
     
    #method of checking the value 
    def add_child(self, data):
        if data == self.data: #see if the value already exists
            return

        #if the data is less than self.data
        if data < self.data: 
            #add data in left subtree
            if self.left: #check if the left element has value
                self.left.add_child(data) #call child method
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.left: #check if the right element has value
                self.left.add_child(data) #call child method
            else:
                self.right = BinarySearchTreeNode(data)
    
    #method that return the list of elements in binary tree in specific order       
    def in_order_traversal(self):
        #add list 
        elements = []
        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

#method that takes elements as an input and build a tree
def build_tree(elements):
    # assigning the first element as a root node
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i]) #child method to build a tree

    return root
