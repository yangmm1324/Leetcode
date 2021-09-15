706. Design HashMap
Easy

Description
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

1. 澄清:
   what is the freq and range of the key number,
   need to know how large of the array size for hashing

2. 易错点:
   linked list implementation
   for head at each location, set unfeasible value(-1), and works as dummy node
   for function of get and remove, check node and node.next instead

   remeber to use the prime as the module size!

3. 思路
   3.1 use array and mod hashing --remove has o(n) time

   3.2 use linked list and mod hashing,--remove could be seen as o(1) time

4.1. algorithm: use array,
class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1003
        self.arr = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        for i, (k, v) in enumerate(self.arr[index]):
            if k == key:
                self.arr[index][i] = [key, value]
                return
        self.arr[index].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key %self.size
        for k, v in self.arr[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        for i, (k, v) in enumerate(self.arr[index]):
            if k == key:
                del self.arr[index][i]

class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1003
        self.list = [ListNode() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key %self.size
        head = self.list[index]
        while head and head.next:
            if head.next.key == key:
                break
            head = head.next
        head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key% self.size
        head = self.list[index]
        while head:
            if head.key == key:
                return head.val
            head = head.next

        return -1
    def remove(self, key: int) -> None:
        index = key% self.size
        head = self.list[index]

        while head and head.next:
            if head.next.key ==key:
                head.next = head.next.next
                return
            head = head.next
