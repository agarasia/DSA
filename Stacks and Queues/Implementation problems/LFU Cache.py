class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_tail(self) -> Node:
        if self.tail.prev == self.head:
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node

    def is_empty(self) -> bool:
        return self.head.next == self.tail

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.cache = {}
        self.freq_map = {}

    def _update_freq(self, node: Node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
        if self.freq_map[freq].is_empty():
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        new_freq = node.freq
        
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        
        self.freq_map[new_freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int):
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq(node)
        else:
            if self.size >= self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                node_to_remove = lfu_list.pop_tail()
                del self.cache[node_to_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.cache[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1
            self.size += 1
