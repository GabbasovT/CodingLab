from typing import List

def move_to_front_transform(s: str) -> str:
    alphabet: str = [chr(i + ord('a')) for i in range(26)]
    result = []

    for char in s:
        index: int = alphabet.index(char)
        result.append(str(index + 1))
        alphabet.remove(char)
        alphabet.insert(0, char)

    return ' '.join(result)

s: str = input()
print(move_to_front_transform(s))
