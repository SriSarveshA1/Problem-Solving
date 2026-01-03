class Node:
    def __init__(self,key,value):
        self.prev = None
        self.key  = key
        self.value = value
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = dict()
    
    def _create_init_list_with_key(self,key,value):
        node = Node(key,value)
        self.head = node
        self.tail = node
        self.map[key] = node

    def _insert_at_head(self,key,value):
        if len(self.map) == 0:
            self._create_init_list_with_key(key,value)
            return
        
        node = Node(key,value)
        self.head.prev = node
        node.next = self.head
        self.head = node

        self.map[key] = node

    def _delete_node_from_list(self,node):
        key = node.key

        if node.prev == None and node.next == None:
            # Deleting the only node
            self.head = None
            self.tail = None

        elif node.prev == None and node.next != None:
            # Deleting the head node.
            temp = self.head.next
            temp.prev = None
            self.head = temp 

        elif node.prev != None and node.next == None:
            # Deleting the tail node
            self.tail = self.tail.prev
            self.tail.next = None

        elif node.prev != None and node.next !=None:
            # Deleting in middle
            node.prev.next = node.next
            node.next.prev = node.prev

        del self.map[key] 


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        # Now the key is there , now we need to re-order it
        # Pick the node which has the key 
            #1.Delete it
            #2.Re-enter it from head
        
        node = self.map[key]
        value = node.value
        self._delete_node_from_list(node)
        self._insert_at_head(key,value)
        
        return value

    def put(self, key: int, value: int) -> None:
        
        if len(self.map) == 0:
            # Case1 when we wanted to newly create a list
            self._create_init_list_with_key(key,value)
            return
        
        if len(self.map) < self.capacity:
            if key in self.map:
                # Delete the current node and insert it from head
                node = self.map[key]
                self._delete_node_from_list(node) # delete it
                self._insert_at_head(key,value) # insert it from head
            else:
                # Just insert it from head
                self._insert_at_head(key,value) # insert it from head
        
        else:
            if key in self.map:
                # Delete the current node and insert it from head
                # Delete the current node and insert it from head
                node = self.map[key]
                self._delete_node_from_list(node) # delete it
                self._insert_at_head(key,value) # insert it from head
            else:
                # Delete the tail node and insert it from head
                self._delete_node_from_list(self.tail) # delete the tail node
                self._insert_at_head(key,value)

        return None



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)