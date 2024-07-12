class Node:
    def __init__(self, key,val):
        self.key=key
        self.val=val
        self.prev,self.next=None,None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}#hashmap to store key-node pair where node pointing to value of its key
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    # node is always middle of other nodes
    #if its first node, then its middle of left and right node
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next,nxt.prev=nxt,prev
    #insert alwasy happens on previous node of right node as its most recent used node
    def insert(self,node):   
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.prev,node.next=prev,nxt
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            #remove left key which is LRU
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)