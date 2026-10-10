## 1. Python Basics
### Foundations & Syntax
- [ ] Variables and dynamic typing
- [ ] Basic data types (int, float, bool, str)
- [ ] Type casting and type checking (`type()`, `isinstance()`)
- [ ] Basic operators (arithmetic, relational, logical, bitwise)
- [ ] String manipulation and formatting (f-strings, `.format()`, slicing)
- [ ] User input and basic console I/O

### Control Flow
- [ ] `if`, `elif`, `else` statements
- [ ] `for` loops and `range()`
- [ ] `while` loops
- [ ] `break`, `continue`, and `pass` statements
- [ ] `match-case` (Python 3.10+ structural pattern matching)

### Functions
- [ ] Defining functions (`def`)
- [ ] Positional and keyword arguments
- [ ] Default parameters
- [ ] `*args` and `**kwargs`
- [ ] Variable scope (Local, Global, `global`, `nonlocal`)
- [ ] Lambda functions (anonymous functions)
- [ ] Higher-order functions (`map()`, `filter()`, `reduce()`)

### Built-in Data Structures
- [ ] Lists (creation, indexing, slicing, methods like `append()`, `pop()`)
- [ ] Tuples (immutability, packing/unpacking)
- [ ] Dictionaries (key-value pairs, `.keys()`, `.values()`, `.items()`)
- [ ] Sets (unique elements, union, intersection, difference)
- [ ] List, Dictionary, and Set comprehensions

### Advanced Pythonic Concepts
- [ ] Iterators and Iterables (`__iter__`, `__next__`)
- [ ] Generators and the `yield` keyword
- [ ] Decorators (function wrappers, `@` syntax)
- [ ] Context Managers (`with` statement)
- [ ] Exception Handling (`try`, `except`, `else`, `finally`, `raise`)
- [ ] File I/O (opening, reading, writing, closing files)
- [ ] Modules and Packages (`import`, `from ... import ...`, `__init__.py`)
- [ ] Type Hinting (`typing` module, `List`, `Dict`, `Optional`)

---

## 2. Object-Oriented Programming (OOP)
### Fundamentals
- [ ] Procedural programming vs OOP
- [ ] Class and object creation
- [ ] State, behavior, and identity of an object
- [ ] Instance, class, and local variables
- [ ] Constructors (`__init__()`) and Destructors (`__del__()`)
- [ ] The `self` parameter
- [ ] Mutable vs immutable objects
- [ ] Object lifecycle and garbage collection

### The Four Pillars
- [ ] **Encapsulation:** Bundling data/methods, public/protected/private modifiers, name mangling, getters/setters, `@property`.
- [ ] **Abstraction:** Hiding implementation, abstract classes (`abc` module, `@abstractmethod`), interfaces, Protocols.
- [ ] **Inheritance:** Single, multiple, multilevel, hierarchical. `super()` function, Method Resolution Order (MRO), Mixins.
- [ ] **Polymorphism:** Method overriding, duck typing, operator overloading, dynamic method dispatch.

### Dunder / Special Methods
- [ ] Object initialization: `__new__`, `__init__`
- [ ] Representation: `__str__`, `__repr__`
- [ ] Comparison: `__eq__`, `__lt__`, `__gt__`
- [ ] Container: `__len__`, `__getitem__`, `__setitem__`, `__contains__`
- [ ] Mathematical operations: `__add__`, `__sub__`
- [ ] Context managers: `__enter__`, `__exit__`
- [ ] Callable: `__call__`

### Python-Specific OOP Features
- [ ] `@classmethod` vs `@staticmethod` vs Instance methods
- [ ] Dataclasses (`@dataclass`)
- [ ] `__slots__` for memory optimization
- [ ] Named tuples
- [ ] Descriptors and Metaclasses (Advanced)

### Class Relationships & Object Model
- [ ] Association, Aggregation, and Composition (Has-a vs Is-a)
- [ ] Dependency and Realization
- [ ] Shallow copy vs Deep copy (`copy` module)
- [ ] Identity (`is`) vs Equality (`==`)
- [ ] Hashability (`__hash__`)

### Design Principles & Patterns
- [ ] **SOLID:** Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.
- [ ] DRY, KISS, YAGNI, Law of Demeter.
- [ ] Favor composition over inheritance.
- [ ] **Creational Patterns:** Singleton, Factory, Builder.
- [ ] **Structural Patterns:** Adapter, Decorator, Facade, Proxy.
- [ ] **Behavioral Patterns:** Observer, Strategy, Command, Iterator.

---

## 3. Data Structures
### A. Foundations
- [ ] Arrays and dynamic arrays
- [ ] Strings and character arrays
- [ ] Matrices and 2D arrays
- [ ] Time and space complexity (Big-O, Big-Theta, Big-Omega)
- [ ] Recursion and the call stack
- [ ] Pointers, references, and memory layout

### B. Linear Data Structures
- [ ] Singly, Doubly, and Circular linked lists
- [ ] Stacks (Array and Linked List implementation)
- [ ] Queues, Circular queues, and Deque
- [ ] Monotonic stack and Monotonic queue

### C. Hash-Based Structures
- [ ] Hash tables / Hash maps / Dictionaries
- [ ] Hash sets
- [ ] Hash functions, collisions, chaining, open addressing
- [ ] Frequency maps and counting

### D. Searching & Ordered Structures
- [ ] Linear and Binary search (Lower/Upper bound)
- [ ] Binary Search Trees (BST) - Search, insertion, deletion
- [ ] Balanced BST concepts (AVL, Red-Black)
- [ ] Ordered sets and maps

### E. Trees
- [ ] Binary tree representations
- [ ] Traversals: Preorder, Inorder, Postorder, Level-order (BFS)
- [ ] Tree properties: Height, depth, diameter, LCA
- [ ] Serialize and deserialize trees
- [ ] Binary Heaps (Min-heap, Max-heap, Priority Queue)
- [ ] Tries / Prefix trees

### F. Graph Data Structures
- [ ] Adjacency matrix, Adjacency list, Edge list
- [ ] Directed/Undirected, Weighted/Unweighted graphs
- [ ] Connected components
- [ ] Disjoint Set Union (DSU) / Union-Find (Path compression, union by rank)

### G. Range-Query & Advanced Structures
- [ ] Prefix sums and difference arrays
- [ ] Segment trees and Binary Indexed Trees (Fenwick Tree)
- [ ] Sparse table
- [ ] LRU Cache (Hash map + Doubly linked list) and LFU Cache

---

## 4. Algorithms
### A. Analysis & Sorting
- [ ] Recurrence relations and Master theorem basics
- [ ] Bubble, Selection, and Insertion sort
- [ ] Merge sort, Quick sort, Heap sort
- [ ] Counting sort, Radix sort, Bucket sort
- [ ] Custom comparator sorting

### B. Two Pointers & Sliding Window
- [ ] Opposite-direction and same-direction pointers
- [ ] Fast and slow pointers (Cycle detection)
- [ ] Sliding window (Fixed and Variable size)
- [ ] Dutch National Flag partitioning

### C. Prefix & Hashing Techniques
- [ ] Prefix sums, Prefix XOR, Difference arrays
- [ ] 2D Prefix sums
- [ ] Subarray sum equals K
- [ ] Grouping by keys, anagram patterns, longest consecutive sequence

### D. Stack & Queue Algorithms
- [ ] Balanced parentheses
- [ ] Next greater/smaller element (Monotonic stack)
- [ ] Largest rectangle in histogram / Stock span
- [ ] Sliding window maximum (Deque)
- [ ] Interval merging, inserting, scheduling

### E. Recursion & Backtracking
- [ ] Subsets, Subsequences, Permutations, Combinations
- [ ] Combination sum, Generate parentheses
- [ ] Word search / grid backtracking
- [ ] N-Queens and Sudoku

### F. Linked-List & Tree Algorithms
- [ ] Reverse list, find middle, detect cycle
- [ ] Merge lists, remove nth node, reorder list
- [ ] Tree height, diameter, balanced validation
- [ ] Root-to-leaf paths, LCA
- [ ] Kth smallest/largest in BST

### G. Heaps & Greedy
- [ ] Top K elements / Kth largest
- [ ] K-way merge (Merge K sorted lists)
- [ ] Two heaps (Running median)
- [ ] Greedy choice property (Activity selection, Jump Game, Gas Station)

### H. Graph Algorithms
- [ ] Graph BFS and DFS (Number of islands, cycle detection)
- [ ] Topological sorting (Kahn's algorithm)
- [ ] Bipartite graph checking
- [ ] Shortest path: Dijkstra's, Bellman-Ford, Floyd-Warshall
- [ ] Minimum Spanning Tree: Kruskal's, Prim's
- [ ] Strongly connected components (Kosaraju/Tarjan)

### I. Dynamic Programming (DP)
- [ ] Memoization (Top-down) vs Tabulation (Bottom-up)
- [ ] 1D DP (Fibonacci, Climbing stairs, House Robber)
- [ ] Grid / 2D DP (Min/Max paths)
- [ ] Knapsack (0/1 and Unbounded), Subset sum, Coin change
- [ ] Longest Increasing Subsequence (LIS)
- [ ] Longest Common Subsequence (LCS) / Edit Distance
- [ ] Interval DP, Matrix-chain multiplication
- [ ] Bitmask DP

### J. Strings, Bit Manipulation & Math
- [ ] String matching (KMP, Rabin-Karp, Z algorithm)
- [ ] Bitwise AND, OR, XOR, shifts, masking
- [ ] Count set bits, Brian Kernighan's algorithm
- [ ] GCD/LCM (Euclidean algorithm), Sieve of Eratosthenes
- [ ] Modular arithmetic, Fast exponentiation