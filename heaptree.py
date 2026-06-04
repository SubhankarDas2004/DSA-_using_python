def heapify(a,i,n):
    
    l=2*i+1
    r=2*i+2
    largest=i
    
    if r<n and a[r]>a[largest]:
        largest=r

    if l<n and a[l]>a[largest]:
        largest=l

    if largest==i:
        return
    
    a[largest],a[i]=a[i],a[largest]
    heapify(a,largest,n)

def maxheap(a,n):
    for i in range((n//2)+1,-1,-1):
        heapify(a,i,n)

def heapsort(a):
    n=len(a)
    while(n>=1):
        a[0],a[n-1]=a[n-1],a[0]
        n=n-1
        heapify(a,0,n)
        

a=[40,30,50,60,35,49,65,55,25,28]
print("before sort",a)
maxheap(a,len(a))
heapsort(a)
print("after sort",a)
