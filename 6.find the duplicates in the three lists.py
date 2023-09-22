a=[1,2,3,4,5,6,7,8,9]; b=[1,89,34,6,23,67]; c=[1,234,111,678,9,6,34]
a1=[]
n=len(a); n1=len(b); n2=len(c)
for i in range(0,n):
          for j in range(0,n1):
                    for k in range(0,n2):
                              if a[i]==b[j]: 
                                        a1.append(a[i])
                              if a[i]==c[k]:
                                        a1.append(a[i])
                              if b[j]==c[k]:
                                        a1.append(c[k])
a1=set(a1)
print('find the duplicates in the three lists :  ' ,a1)
