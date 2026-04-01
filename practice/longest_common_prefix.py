# HORIZONTAL SCANNING

def lcp(arr):
    if not arr:
        return ""
    prefix=arr[0]
    for s in arr[1:]:
        while s.find(prefix)!=0:
            prefix=prefix[:-1]
            if not prefix:
                return ""
            
    return prefix

strs = ["flower","flow","flight"]
print(lcp(strs))

# VERTICAL SCANNING
def lcp_vertical(arr):
    if not arr:
        return ""
    for i in range(len(arr[0])):
        ch = arr[0][i]
        for s in arr[1:]:
            if i >= len(s) or s[i] != ch:
                return arr[0][:i]
    return arr[0]

print(lcp_vertical(strs))