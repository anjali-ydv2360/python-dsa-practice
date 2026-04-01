p=int(input())
q=int(input())
r=int(input())
def min_ops(p,q,r):
    if p==q and q==r:
        return 0
    arr=[p,q,r]
    arr.sort()
    step=0
    while(True):
        arr[0]+=1
        arr[1]+=1
        arr[2]-=1
        step+=1
        if arr[0]==arr[1] and arr[1]==arr[2]:
            return step
        arr.sort()
        if (arr[0]==arr[1] and arr[1]+1==arr[2]) or (arr[1]==arr[2] and arr[0]+1==arr[1]):
            #if (p + q + r) % 3 != 0: return -1  we can also write this condition
            return -1
print("ops needed:", min_ops(p,q,r))
