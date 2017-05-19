""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    status = True
    print 'current root', root.data

    if root.left != None and root.left.data < root.data:
        if root.left.right != None and root.left.right.data < root.data:
            status = check_binary_search_tree_(root.left)
        elif root.left.right == None:
            status = check_binary_search_tree_(root.left)
        else:
            print '1 got false'
            return False
    if root.right != None and root.right.data > root.data:
        if root.right.left != None and root.right.left.data > root.data:
            status = check_binary_search_tree_(root.right)
        elif root.right.left == None:
            status = check_binary_search_tree_(root.right)
        else:
            print '2 got false', root.data
            return False
    if root.left != None and root.left.data >= root.data:
        print '3 root.left.data', root.left.data, 'root.data ', root.data
        return False
    if root.right != None and root.right.data <= root.data:
        print '4 root.right.data', root.right.data, 'root.data ', root.data
        return False
    #print 'no right or left root!'
    print status
    return status


