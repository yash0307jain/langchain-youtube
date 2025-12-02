# **1. Introduction to Data Structures**

### **Theory**

A **data structure** is a method of organizing data in memory so that it can be efficiently accessed and modified.
Operations like searching, insertion, deletion, traversal depend on how data is organized.

Examples:
Arrays, Linked Lists, Trees, Graphs, Hash Tables, etc.

---

# **2. Arrays**

### **Theory**

-   Stores elements in **contiguous memory**.
-   Index-based **O(1)** access.
-   Insertion/deletion in middle = **O(n)** due to shifting.

### **Code**

```python
# Array in Python (using list)
arr = [10, 20, 30, 40]

# Access
print(arr[2])  # Output: 30

# Insert
arr.append(50)

# Delete
arr.remove(20)

print(arr)
```

---

# **3. Linked List**

### **Theory**

A **linked list** stores elements as **nodes** containing:

-   Data
-   Pointer/reference to next node

Advantages:
✔ Dynamic size
✔ Fast insertion/deletion at beginning (**O(1)**)

Disadvantages:
✘ Slow access (**O(n)**)

### **Code**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.print_list()
```

---

# **4. Stack (LIFO)**

### **Theory**

A **stack** works on **Last In, First Out** principle.
Used in recursion, undo operations, expression evaluation.

### **Code**

```python
stack = []

# Push
stack.append(10)
stack.append(20)

# Pop
print(stack.pop())  # Output: 20
```

---

# **5. Queue (FIFO)**

### **Theory**

Queue follows **First In, First Out** ordering.
Used in BFS, job scheduling, task queues.

### **Code**

```python
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
print(queue.popleft())  # Output: 10
```

---

# **6. Binary Tree & Traversal**

### **Theory**

A **binary tree** is a hierarchical structure where each node has at most two children.
**Inorder traversal** gives sorted order for BSTs.

### **Code**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

inorder(root)
```

---

# **7. Binary Search Tree (BST)**

### **Theory**

A **BST** maintains sorted structure:

-   Left subtree < root
-   Right subtree > root

Supports efficient **O(log n)** search, insert.

### **Code**

```python
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.data:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insert(val)

# Usage
root = BST(10)
root.insert(5)
root.insert(20)
```

---

# **8. Heap**

### **Theory**

A **heap** is a complete binary tree with heap property:

-   **Min heap**: parent <= children
    Used for priority queues.

### **Code**

```python
import heapq

# Min heap (default)
heap = []

heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)

print(heapq.heappop(heap))  # Output: 5
```

---

# **9. Hash Table (Dictionary)**

### **Theory**

A hash table stores **key-value** pairs with average **O(1)** access.
Python dictionaries are built using hash tables.

### **Code**

```python
# Python dictionary as hash table
hash_table = {
    "name": "Alice",
    "age": 25
}

# Insert
hash_table["city"] = "New York"

# Access
print(hash_table["name"])

# Delete
del hash_table["age"]
```

---

# **10. Sorting Algorithms**

---

## **Bubble Sort**

### **Theory**

Repeatedly compares adjacent elements and swaps them.

-   Time: **O(n²)**
-   Space: **O(1)**
    Simple but inefficient.

### **Code**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 1, 4, 2]))
```

---

## **Merge Sort**

### **Theory**

A **divide-and-conquer** algorithm:

1. Split
2. Sort recursively
3. Merge

-   Time: **O(n log n)**
-   Space: **O(n)**

### **Code**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print(merge_sort([5, 1, 4, 2]))
```

---

## **Quick Sort**

### **Theory**

Divide-and-conquer algorithm:

1. Select pivot
2. Partition
3. Recursively sort

-   Avg time: **O(n log n)**
-   Worst: **O(n²)**

### **Code**

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([5, 1, 4, 2]))
```

---

# **11. Searching Algorithms**

---

## **Linear Search**

### **Theory**

Checks every element until the target is found.

-   Time: **O(n)**
-   Works on unsorted data.

### **Code**

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

---

## **Binary Search**

### **Theory**

Works only on sorted arrays.

-   Time: **O(log n)**
-   Uses divide-and-conquer.

### **Code**

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1,2,3,4,5], 4))
```

---

# **12. Recursion**

### **Theory**

A function calling itself with a smaller subproblem.
Requires:

-   Base case
-   Recursive relation

### **Code**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

---

# **13. Graphs (BFS + DFS)**

---

### **Theory**

A graph is a collection of nodes (vertices) connected by edges.
**Traversal methods**:

-   BFS → level order
-   DFS → depth-first

---

## **BFS Code**

```python
from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(1)
```

---

## **DFS Code**

```python
def dfs(node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

dfs(1)
```

---

# **14. Greedy Algorithm (Activity Selection)**

### **Theory**

A greedy algorithm makes the **locally optimal choice** at every step.
Activity selection picks the maximum number of non-overlapping intervals.

### **Code**

```python
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # sort by finish time
    result = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= result[-1][1]:
            result.append(activities[i])

    return result

print(activity_selection([(1,3),(2,5),(4,6)]))
```

---

# **15. Dynamic Programming (DP)**

---

## **Fibonacci (Memoization)**

### **Theory**

Memoization stores previously computed values to avoid redundant calculations.

### **Code**

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(10))
```

---

## **0/1 Knapsack**

### **Theory**

DP is used to handle choices like:

-   Include item
-   Exclude item

`dp[i][w]` = best value using first `i` items and capacity `w`.

### **Code**

```python
def knapsack(weights, values, W):
    n = len(values)
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

print(knapsack([1,2,3], [6,10,12], 5))
```
