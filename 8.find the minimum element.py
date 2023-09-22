a=[10,501,22,37,100,87,351,5]
n=len(a)
for i in range(0,n,1):
          for j in range(i+1,n,1):
                    if(a[i]>a[j]):
                              p=a[i]
                              a[i]=a[j]
                              a[j]=p
          print('minimum element is : ',a[i])
          break
