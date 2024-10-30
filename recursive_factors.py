from functools import lru_cache
import math
import time

PRIMES = [2]


@lru_cache
def factor(n):
    # if n in PRIMES:
    #     return [1, n]
    # out = []
    # for a in PRIMES:
    #     if n % a == 0:
    #         out.append(a)
    #         out.append(int(n/a))
    # if len(out) == 0:
    #     PRIMES.append(n)
    #     return factor(n)
    # out += [1, n]
    # out = list(set(out))
    # out.sort()
    # return out
    out = []
    for a in range(1, int(math.sqrt(n))+1):
        if n % a == 0:
            out.append(a)
    out2 = []
    for b in out:
        out2.append(int(n/b))
    out2 += out
    out2 = list(set(out2))
    out2.sort()
    return out2


start = time.time()
print(len(factor(94547089752615745945)))
print(time.time()-start)
