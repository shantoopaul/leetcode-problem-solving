class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        total = 1 << k
        
        if n - k + 1 < total:
            return False
        
        mask = total - 1
        seen = [False] * total
        curr = count = 0
        
        for i, ch in enumerate(s):
            curr = ((curr << 1) & mask) | (ch == '1')
            
            if i >= k - 1 and not seen[curr]:
                seen[curr] = True
                count += 1
                if count == total:
                    return True
        
        return False