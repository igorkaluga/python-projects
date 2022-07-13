#Sets up the arr to contain a large file of unsorted integers to run mergeSortInverse function on.
f = open("#", "r")
arr = []
for i in f:
    arr.append(int(i))

#Function itself
def mergeSortInv(arr):
    if len(arr) == 1:
        #base case
        return arr, 0
    else:
        a = arr[:len(arr)//2] # left side of the arr
        b = arr[len(arr)//2:] # right side of the arr
        
        a, ai = mergeSortInv(a)
        b, bi = mergeSortInv(b)
        
        c = [] #ordered list of a and b arrays
        
        i = j = 0
        inversion = 0 + ai + bi # adds the past inverisons from case below to total
        
        while i < len(a) and j < len(b):
            #i iterates over a array (left side)
            #j iterates over b array (right side)
            
            if a[i] <= b[j]:
                c.append(a[i]) #append current val from a array
                i += 1  # increment i pointer
            else:
                c.append(b[j]) #append current val from b arr
                j += 1 # incement j pointer
                inversion += len(a[i:])
                
        #once one the loop ends, add the rest of the arrays
        #to c
        
        c += a[i:]
        c += b[j:]
        
    return c, inversion
    
    
mergeSort(arr)
