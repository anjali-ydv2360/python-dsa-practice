def find_single(arr):
    result = 0
    arr.sort() # Sorting the array is not necessary for the XOR method, but it can help in understanding the problem.
    
    for num in arr:
        result ^= num
    
    return result

arr = [2, 3, 5, 3, 2, 4, 4]
print("Single element:", find_single(arr))