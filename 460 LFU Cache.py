460. LFU Cache
Hard

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present.
When the cache reaches its capacity,
it should invalidate and remove the least frequently used key before inserting a new item.
For this problem, when there is a tie (i.e., two or more keys with the same frequency),
the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache.
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
The use counter for a key in the cache is incremented either a get or put operation is called on it.


Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3



1. 澄清:


2. 易错点:
   maintain the minfreq and def len function for the double link list
   when adding a new node, need to remove the least used node first if exceeds the capacity

3. 思路
   3.1 double linked list + freq hashtable of double linklist + minfreq
       Node class for double link list
       Double link list class for freq to easy add and remove
               append to the last
               pop for remove node and popleft

       LFU class with following function
               update(node) for set and get call function
               set
               get
                  note that the minfreq will start over when you add new key


4.1.algorithm: use double linked list, o(1) time for get and put

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.root = Node(None, None)
        self.root.next = self.root.prev = self.root
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.root.next
        self.root.next.prev = node
        node.prev = self.root
        self.root.next = node
        self.size += 1

    def pop(self, node = None):
        if self.size == 0:
            return
        if node == None:
            node = self.root.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

class LFUCache:
    def __init__(self, capacity):
        self.size = 0
        self.cache = {}
        self.freq = collections.defaultdict(DoubleList)
        self.minfreq = 0

    def update(self, node):
        freq = node.freq
        self.freq[freq].pop(node)
        if node.freq == self.minfreq and not self.freq[self.minfreq]:
            self.minfreq += 1
        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val

    def put(self, key, value):
        if self.cap == 0: return
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.cap:
                node = self.freq[self.minfreq].pop()
                del self.cache[node.key]
                self.size -= 1

            node = Node(key, value)
            self.minfreq = 1
            self.size += 1
            self.freq[1].append(node)
            self.cache[key] = node
