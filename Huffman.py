from typing import List, Dict, Tuple
import heapq

n: int = int(input())
bytes_frequencies: Dict[int, int] = {i: int(x) for i, x in enumerate(input().split())}
bytes_frequencies_list: List[Tuple[int, int]] = list(bytes_frequencies.items())
answer: int = 0


class Node:
    def __init__(self, freq: int, byte: int = -1, left: 'Node' = None, right: 'Node' = None):
        self.freq = freq
        self.byte = byte
        self.left = left
        self.right = right
        self.huffman_code = ''

    def __lt__(self, other: 'Node') -> bool:
        return self.freq < other.freq


def build_huffman_tree(bytes_frequencies: Dict[int, int]) -> Node:
    heap = [Node(freq, byte) for byte, freq in bytes_frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, -1, left, right)
        heapq.heappush(heap, merged)
    return heap[0]


def len_of_text(vertex: Node, depth: int = 0):
    global answer
    if vertex is None:
        return
    if vertex.byte != -1:
        answer += vertex.freq * depth
    len_of_text(vertex.left, depth + 1)
    len_of_text(vertex.right, depth + 1)
huffman_tree: Node = build_huffman_tree(bytes_frequencies)
len_of_text(huffman_tree)
print(answer)
