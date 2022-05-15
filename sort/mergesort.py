def mergesort(a):
    '''
    This is the python code for sorting array using mergesort algorithm.
    Test seed: a= [ 113,345, 98239,198,92,5,534,6,456,12,3,32,345,34,6,54,7,56]
    '''
    if len(a)>1:
        mid = len(a)/2
        lefthalf = a[:mid]
        righthalf = a[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i]<righthalf[j]:
                a[k] = lefthalf[i]
                i=i+1
            else:
                a[k] = righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            a[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            a[k]=righthalf[j]
            j=j+1
            k=k+1
            
if __name__ == '__main__':
    a = [113,345,98239,198,92,5,534,6,456,12,3,32,345,34,6,54,7,56] # test seed
    print(a)
    mergesort(a)
    print(a)