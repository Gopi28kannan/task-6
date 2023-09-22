def a(k,o):
    for i in range(o-1):
        s=k[i]
        for j in range(i+1,o):
            s+=k[j]
            if s==0:
                return True
    return False
b=[4,2,-3,1,6]
print(a(b,len(b)))
