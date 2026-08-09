class Node: 
    def __init__(self, key, value):
         self.key = key
         self.value = value
         self.next = None
         self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # head = LRU, tail = MRU 
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # self.remove a given node from the LinkedList
    def remove(self, node):
        # get pointers to prev and curr
        prev, nxt = node.prev, node.next
        # update pointers of prev and curr
        prev.next, nxt.prev = nxt, prev

    
    # insert node to the tail of the linkedlist
    def insertTail(self, node):
        # get pointers to current and prev
        prev, nxt = self.tail.prev, self.tail 
        # insert it in the middle
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        # if in hashmap, return
        if key in self.cache:
            # self.remove node and place it at tail
            node = self.cache[key]
            self.remove(node)
            self.insertTail(node)
            return self.cache[key].value
        return -1



    def put(self, key: int, value: int) -> None:
        # if node already exists, self.remove from linkedlist
        if key in self.cache: 
            self.remove(self.cache[key])
        # create a new node
        node = Node(key, value)
        self.cache[key] = node
        # if capacity is exceeded
        if len(self.cache) > self.capacity:
            # remove the head 
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        # add the new node to MRU
        self.insertTail(node)

        





        
