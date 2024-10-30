from functools import lru_cache


BREAKS = [1]


# @lru_cache
def _collatz(n, ct=0, seed=0):
    if n in BREAKS:
        BREAKS.append(seed)
        return [0, ct]
    if n % 2 == 0:
        return _collatz(int(n/2), ct + 1, n if seed == 0 else seed)
    else:
        return _collatz(3*n+1, ct + 1, n if seed == 0 else seed)


total = 0
for a in range(1, 1000):
    b = _collatz(a)
    if b[0] == 0:
        BREAKS.append(a)
    total += b[1]

print(total)
