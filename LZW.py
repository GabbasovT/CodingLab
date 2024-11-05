from typing import List, Dict

def lzw_encode(s: str) -> List[int]:
    dictionary: Dict[str, int] = {chr(i + ord('a')): i for i in range(26)}
    result: List[int] = []
    current_buffer: str = ""

    for char in s:
        new_buffer: str = current_buffer + char
        if new_buffer in dictionary:
            current_buffer = new_buffer
        else:
            result.append(dictionary[current_buffer])
            dictionary[new_buffer] = len(dictionary)
            current_buffer = char

    if current_buffer:
        result.append(dictionary[current_buffer])

    return result

s: str = input()
print(' '.join(map(str, lzw_encode(s))))
