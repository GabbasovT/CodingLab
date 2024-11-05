from typing import List

def lzw_decode(n: int, codes: List[int]) -> str:
    dictionary = {i: chr(i + ord('a')) for i in range(26)}
    result = []
    current_buffer = dictionary[codes[0]]
    result.append(current_buffer)

    for code in codes[1:]:
        if code in dictionary:
            entry = dictionary[code]
        else:
            entry = current_buffer + current_buffer[0]
        result.append(entry)
        dictionary[len(dictionary)] = current_buffer + entry[0]
        current_buffer = entry

    return ''.join(result)

n: int = int(input())
codes = list(map(int, input().split()))
decoded_string = lzw_decode(n, codes)
print(decoded_string)
