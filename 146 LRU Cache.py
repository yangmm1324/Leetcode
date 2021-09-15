146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

1. 澄清:
   when get and put function will count as use?

2. 易错点:
   when evict the nodes when exceed capacity, be careful with the evict condition == or >, as we did not remove from the self.cache first, so use > instead

3. 思路
   3.1 use deque and hashtable, get and put will have time o(n) time

   3.2 use double linked list
   to avoid the edge cases for deletion and insert, we use dummy head and dummy tail, save a lot of trouble!!!

4.1.algorithm: use deque, o(n) time| o(capacity) space
class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.queue = collections.deque([])
        self.cap = capacity

    def get(self, key):
        if key not in self.cache: return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        self.queue.append(key)
        self.cache[key] = value
        if len(self.queue) > self.cap:
            pop = self.queue.popleft()
            del self.cache[pop]

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self,capacity):
        self.cache = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        if len(self.cache)> self.cap:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        last = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev = last
        last.next = node
