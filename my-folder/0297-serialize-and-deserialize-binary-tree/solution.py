# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import ast
import json

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # li = []
        # if not root:
        #     return str('[]')
        
        # temp = [root]
        # while temp:
        #     te = temp.pop(0)
        #     if te == None:
        #         li.append(None)
        #     else:
        #         li.append(te.val)
        #         temp.append(te.left)
        #         temp.append(te.right)
        # i = 0
        # while li and li[-1]==None:
        #     li.pop(-1)

        # # python_list = ast.literal_eval(li)

        # # 2. Replace the string 'null' with Python's None
        # output = json.dumps(li)
        # # output = json.dumps(parsed_list, separators=(',', ':'))
        # return output
        if not root:
            return ""
        serialized_list = []

        def preorder_serializer(node, serialized_list):
            if not node:
                serialized_list.append("#")
                return
            serialized_list.append(str(node.val))
            preorder_serializer(node.left, serialized_list)
            preorder_serializer(node.right, serialized_list)
            return serialized_list

        preorder_serializer(root, serialized_list)
        return ','.join(serialized_list)



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # data = json.loads(data)
        # le = len(data)
        # if le ==0 or data[0]== None:
        #     return []

        # root = TreeNode(data[0])
        # li=[]
        # li.append((root,0))
        # nc=0
        # while(li):
        #     temp= li.pop(0)
        #     node = temp[0]
        #     idx=temp[1]
        #     print(idx)
        #     if temp[0]==None:
        #         continue
        #     fci=2*(idx+1)-1
        #     sci=2*(idx+1) 
        #     fcv = data[fci] if fci<le  else None
        #     scv = data[sci] if sci<le  else None
        #     if fcv:
        #         node.left=TreeNode(fcv)
        #         li.append((node.left,fci))
        #     if scv:
        #         node.right=TreeNode(scv)
        #         li.append((node.right,sci))
        #     # print(li)

        # return root
        
        # vals = iter(data.split(","))
        # print(vals)
        # def build():
        #     v = next(vals)
        #     if v == None: return None
        #     node = TreeNode(v)
        #     node.left = build()
        #     node.right = build()
        #     return node
        # return build()
        print("Data: ", data)

        if not data:
            return None

        def preorder_deserializer(values):
            val = next(values)
            print(val)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = preorder_deserializer(values)
            node.right = preorder_deserializer(values)
            return node
        
        values = iter(data.split(","))
        return preorder_deserializer(values)
        # nodeValues = json.loads(data)
        # self.i = 0

        # def construct():
        #     nodeVal = nodeValues[self.i]
        #     self.i += 1
        #     if nodeVal == None:
        #         return None
        #     node = TreeNode(nodeVal)
        #     node.left = construct()
        #     node.right = construct()
        #     return node
        
        # return construct()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
