from typing import List

def burrows_wheeler_transform(s: str) -> str:
    cyclic_shifts: List[str] = [s[i:] + s[:i] for i in range(len(s))]
    cyclic_shifts.sort()
    return ''.join(shift[-1] for shift in cyclic_shifts)

s = input()
print(burrows_wheeler_transform(s))
