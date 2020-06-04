"""
428. Serialize and Deserialize N-ary Tree

Add to List

Share
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree
                1
        
    3           2           4

5       6       

as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.
Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.
                                1
            2           3               4           5
                    6       7           8       9       10       
                           11          12      13
                           14

For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].
You do not necessarily need to follow the above suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Codec:
    def serialize(self, root: 'Node') -> str:
        #Encodes a tree to a single string.
        
        #:type root: Node
        #:rtype: str
        
        
	
    def deserialize(self, data: str) -> 'Node':
        #Decodes your encoded data to tree.
        
        #:type data: str
        #:rtype: Node 
"""
from typing import List

class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
class Codec:
    def serialize(self, root: Node) -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        queue = [(root, 0)]
        ans=""
        currLevel=0
        while len(queue) > 0:
            top = queue[0]
            if(currLevel != top[1]):
                ans+="|"+str(top[0].val)
                currLevel=top[1]
            for n in top[0].children:
                queue.append((n, currLevel+1))
            del(queue[0])
        print(ans)
        return ans
	
    def deserialize(self, data: str) -> Node:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

n5=Node(5)
n6=Node(5)
n2=Node(2)
n4=Node(4)
n3=Node(3, [n2,n5,n6])
root=Node(1, [n3, n2, n4])

codec = Codec()
input=root
expected=root
output = codec.deserialize(codec.serialize(root))
print('input %s:'% input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))

