# This code constructs a binary search tree from an array of numbers
# Then it does in-order traverse of the binary search tree to check of it is indeed a BST
# The output will always be yes because the method to check BST is given an input that is binary search tree in this code
# Recursive and iterative versions of BST construction are included

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

nums = [6,2,3,1,8,7,9]


root = node(nums[0])

# recursive insertion
def construct(num, loc):
    if (num > loc.data and loc.right is None):
        r_ch=node(num)
        loc.right=r_ch
        return
    if ( num <loc.data and loc.left is None):
        l_ch=node(num)
        loc.left=l_ch
        return
    if (num > loc.data and loc.right is not None):
        construct(num, loc.right)
    if nums<loc.data and loc.left is not None:
        construct(num,loc.left)
'''
# iterative insertion

def construct(num,loc):
    while( (loc.right is not None and loc.data <num) or ( loc.left is not None and loc.data> num)):
        if loc.data > num:
            loc = loc.left
        else:
            loc=loc.right
    if loc.data > num:
        l_ch = node(num)
        loc.left=l_ch
    else:
        r_ch=node(num)
        loc.right=r_ch

'''
arr = []


def in_order(root):
    if root.left is not  None:
        in_order(root.left)
    arr.append(root.data)
    if root.right is not None:
        in_order(root.right)


def checkBST(root):
    in_order(root)
    temp= arr[0]
    for i in range(1,len(arr)):
        if temp >=  arr[i]:
            print False
        temp = arr[i]
    print True



for i in range(1,len(nums)):
    construct(nums[i],root)

checkBST(root)
