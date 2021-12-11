# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        #### define a function to find the target value
        def find(node:TreeNode, target: int, path:List[str]) -> bool:
            if node.val == target: return True
            if node.left and find(node.left, target, path):
                path += 'L'
                return True
            elif node.right and find(node.right, target, path):
                path += 'R'
                return True
            return False
        
        ###### find the paths from root to the startValue and destValue
        path_s = []; path_d = []
        find(root, startValue, path_s)
        find(root, destValue, path_d)
        
        ###### pop out the common ancesters of the two paths. change the rest of the path to startValue to "U"s and connect it to the rest of the path to the destValue
        while len(path_s) and len(path_d) and path_s[-1] == path_d[-1]:
            path_s.pop()
            path_d.pop()
        return "".join('U'*len(path_s)) + "".join(reversed(path_d))
