def quicksort(a):
    '''This is a function for sorting an array in python using quicksort algorithm.'''
    quicksorthelper(a,0,len(a)-1)

def quicksorthelper(a,first,last):
    if first<last:
        splitpoint = partition(a,first,last)

        quicksorthelper(a,first,splitpoint-1)
        quicksorthelper(a,splitpoint+1,last)

def partition(a,first,last):
    pivot = a[first]

    leftmark = first + 1
    rightmark = last
    flag = False
    while flag == False:
        while leftmark<=rightmark and a[leftmark] <= pivot:
            leftmark = leftmark+1
        while rightmark>=leftmark and a[rightmark] >= pivot:
            rightmark = rightmark -1
        if rightmark<=leftmark:
            flag = True
        else:
            temp = a[leftmark]
            a[leftmark] = a[rightmark]
            a[rightmark] = temp
    temp = a[first]
    a[first] = a[rightmark]
    a[rightmark] = temp

    return rightmark

    
