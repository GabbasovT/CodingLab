from typing import List, Dict

def inverse_burrows_wheeler_transform(bwt: str) -> str:
    count: Dict[str, int] = {}

    for char in bwt:
        count[char] = count.get(char, 0) + 1

    sorted_chars: List[str] = sorted(count.keys())
    first_occurrence: Dict[str, int] = {}
    total: int = 0

    for char in sorted_chars:
        first_occurrence[char] = total
        total += count[char]

    n: int = len(bwt)
    next_indices: List[int] = [0] * n
    count = {char: 0 for char in count}

    for i in range(n):
        char: str = bwt[i]
        next_indices[i] = first_occurrence[char] + count[char]
        count[char] += 1

    original_string: List[str] = []
    index = min(range(n), key=lambda i: bwt[i])

    for _ in range(n):
        original_string.append(bwt[index])
        index = next_indices[index]

    return ''.join(original_string[::-1])


bwt_input: str = input()
result = inverse_burrows_wheeler_transform(bwt_input)
arr: List[str] = [result[i:] + result[:i] for i in range(len(result))]
arr.sort()
print(arr[0])
