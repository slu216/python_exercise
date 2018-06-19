def heapsort(a):
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
                
    for start in xrange(len(a)/2-1,-1,-1):
        shiftDown(a,start,len(a)-1)
    for end in xrange(len(a)-1,0,-1):
        a[0],a[end]=a[end],a[0]
        shiftDown(a,0,end-1) 
#shiftDown 是将堆一路向下沉,直到end结束
