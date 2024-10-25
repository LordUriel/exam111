#1b
#2b
#3a
#4a
#5c
#6a
#7c
#7.1c
#8c
#9a
#10d
#11b
#12b
#13
#14
#15c
#16a
#17b
#18c
#1,1a 1,2b
#2
# import heapq

#class Node:
#    def __init__(self, char, freq):
#       self.char = char  
#        self.freq = freq  
#        self.left = None   
#        self.right = None 
#
#    def __lt__(self, other):
#        return self.freq < other.freq

#def build_huffman_tree(char_freq):
#    heap = [Node(char, freq) for char, freq in char_freq.items()]
#    heapq.heapify(heap)

#    while len(heap) > 1:
#        left = heapq.heappop(heap)
#        right = heapq.heappop(heap)
#
#        merged = Node(None, left.freq + right.freq)
#        merged.left = left
#        merged.right = right

#        heapq.heappush(heap, merged)

#    return heap[0]

#def generate_huffman_codes(node, prefix="", code_dict={}):
#    if node is not None:
#        if node.char is not None:
#           code_dict[node.char] = prefix
#        generate_huffman_codes(node.left, prefix + "0", code_dict)
#       generate_huffman_codes(node.right, prefix + "1", code_dict)
#    return code_dict

#char_freq = {
#    'a': 5,
#   'b': 9,
#    'c': 12,
#    'd': 13,
#    'e': 16,
#    'f': 45
#}

#root = build_huffman_tree(char_freq)

#huffman_codes = generate_huffman_codes(root)

#for char, code in huffman_codes.items():
#    print(f"Character: {char}, Huffman Code: {code}")
#Character: a, Huffman Code: 1100
#Character: b, Huffman Code: 1101
#Character: c, Huffman Code: 100
#Character: d, Huffman Code: 101
#Character: e, Huffman Code: 111
#Character: f, Huffman Code: 0



#3
#def bubble_sort(arr):
#    n = len(arr)
#    for i in range(n):
#        for j in range(0, n - i - 1):
#            if arr[j] > arr[j + 1]:
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#arr = [64, 34, 25, 12, 22, 11, 90]
#bubble_sort(arr)
#print("Sorted array using Bubble Sort:")
#print(arr)
#def insertion_sort(arr):
#    for i in range(1, len(arr)):
#        key = arr[i]
#        j = i - 1
#        while j >= 0 and key < arr[j]:
#            arr[j + 1] = arr[j]
#            j -= 1
#        arr[j + 1] = key
#arr = [64, 34, 25, 12, 22, 11, 90]
#insertion_sort(arr)
#print("Sorted array using Insertion Sort:")
#print(arr)
#Bubble Sort:
#[11, 12, 22, 25, 34, 64, 90]
#Insertion Sort:
#[11, 12, 22, 25, 34, 64, 90]







#3 a




#4
#class Node:
#    def __init__(self, key):
#        self.key = key
#        self.left = None
 #       self.right = None

#class BST:
#    def __init__(self):
#        self.root = None

 #   def insert(self, key):
 #       def _insert_recursive(node, key):
 #           if node is None:
  #              return Node(key)
    #        elif key < node.key:
   #             node.left = _insert_recursive(node.left, key)
   #         else:
   #             node.right = _insert_recursive(node.right, key)
   #         return node

   #     if self.root is None:
   #         self.root = Node(key)
   #     else:
   #         self.root = _insert_recursive(self.root, key)

   # def find_min(self):
   #     current = self.root
   #     while current.left is not None:
   #         current = current.left
    #    return current.key

   # def find_max(self):
   #     current = self.root
   #     while current.right is not None:
    #        current = current.right
   #     return current.key

   # def search(self, key):
   #     def _search_recursive(node, key):
    #        if node is None:
    #            return False
    #        if key == node.key:
    #            return True
    #        elif key < node.key:
    #            return _search_recursive(node.left, key)
     #       else:
     #           return _search_recursive(node.right, key)
#Minimum value in the BST: 5
#Maximum value in the BST: 30
#Searching for 15: Found
#Searching for 100: Not Found




#4b