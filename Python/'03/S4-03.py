#Written by Arghya Vyas
import sys
def suffixarray(s):
    n = len(s)
    suffixes = sorted((s[i:], i) for i in range(n))  # (suffix, index)
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def lcparray(s, suffix_array):
    n = len(s)
    rank = [0] * n
    lcp = [0] * (n - 1)
    
    for i, sa in enumerate(suffix_array):
        rank[sa] = i
    
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return lcp

def cdistinct(s):
    n = len(s)
    suffix_array = suffixarray(s)
    lcp = lcparray(s, suffix_array)
    
    total_substrings = 0
    for i in range(n):
        suffix_length = n - suffix_array[i]
        lcp_length = lcp[i - 1] if i > 0 else 0
        total_substrings += suffix_length - lcp_length
    
    return total_substrings


n = int(sys.stdin.readline().strip())
inputs = [sys.stdin.readline().strip() for _ in range(n)]

results = []
for string in inputs:
    count = cdistinct(string)
    results.append(count)

for result in results:
    print(result+1)
