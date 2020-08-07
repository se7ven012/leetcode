# 给定一个二叉树，返回它的中序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]

# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉树遍历可以用栈迭代实现
# 这里我们把树的结构用两种颜色表示 （灰，白） 
# 这样写出来不会烧脑 
# 1.新节点是白色，已访问节点为灰色
# 2.遇到白色节点将其标灰，并将其右子节 自身 左子节入栈
# 3.遇到的节点为灰色则将该结点的值输出

# 这个方法同样能用在二叉树前序，后序遍历上
# 只要改一下左右子节点入栈顺序即可
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0,1
        res = []
        stack = [(white,root)]
        while stack:
            color,node = stack.pop()
            if not node: continue
            if color == white:
                stack.append((white,node.right))
                stack.append((gray,node))
                stack.append((white,node.left))
            else:
                res.append(node.val)
        return res
