def heapsort(a):
    for start in range(len(a)/2-1,-1,-1):
        shiftDown(a,start,len(a)-1)
    for end in range(len(a)-1,0,-1):
        a[0],a[end]=a[end],a[0]
        shiftDown(a,0,end-1) 
#shiftDown 是将堆一路向下沉,直到end结束
def shiftDown(a,start,end):
    root = start 
    while root*2+1<=end:
        child = root*2+1
        if child + 1 <= end and a[child]<a[child+1]:
            child= child+1
        if child <=end and a[root]<a[child]:
            a[root],a[child] = a[child], a[root]
            root=child
        else:
            return

if __name__ == '__main__':
    a = [113,345,98239,198,92,5,534,6,456,12,3,32,345,34,6,54,7,56] # test seed
    print(a)
    heapsort(a)
    print(a)
