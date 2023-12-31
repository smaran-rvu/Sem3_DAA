def Pivot(l, p, r, pi):
    pivot = l[pi]
    swaps = 0
    i = p-1
    
    for j in range(p, r):
        if l[j] <= pivot:
            i += 1
            if l[j] != l[i]:
                swaps += 1
            # print("swapping", l[j],"<->",l[i])
            l[i], l[j] = l[j], l[i]
            
    l[pi], l[i+1] = l[i+1], l[pi]
    return i+1, swaps+1

def Quick_Sort(l,low,high):
    if low<high:
        # for i in range(1000000): pass
        pivot_index = Pivot(l,low,high,0)
        print(l[low:high+1], low, high, pivot_index)
        Quick_Sort(l, low, pivot_index-1)
        Quick_Sort(l, pivot_index+1, high)

n = int(input())

if n==0:
    print(-1)

else:
    str = input().rstrip()
    l = str.split(' ')
    l = [eval(i) for i in l]

    if n==1:
        print(l[0])
    
    else:
        Quick_Sort(l, 0, len(l)-1)
        for i in l: print(i, end = ' ')