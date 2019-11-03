def mergesort(arr, l, r):
    if r-l ==0:
        return arr, 0
    
    if l < r :
        mid = (l + r) // 2 
        a1, inv1 = mergesort(arr[l : mid + 1], 0, mid - l)
        a2, inv2 = mergesort(arr[mid + 1 : r + 1], 0, r - mid - 1)
        k = l
        i = 0 
        j = 0
        inv = 0
        while i <= mid - l and j <= r - mid - 1 :
            if a1[i] <= a2[j] :
                arr[k] = a1[i]
                i += 1
                k += 1
            else:
                arr[k] = a2[j]
                inv += mid - l - i + 1
                j += 1
                k += 1 
        
        while i <= mid - l :
            arr[k] = a1[i]
            i += 1
            k += 1
        while j <= r - mid -1 :
            arr[k] = a2[j]
            k += 1
            j += 1 
        
        return arr, inv1 + inv2 + inv
            
if __name__ == "__main__" : 
    print("enter the array : ")
    inp = input()
    inp = inp.split()
    l = [int(val) for val in inp]
    arr, ans = mergesort(l, 0, len(l) - 1)
    print("ans: ",ans)


