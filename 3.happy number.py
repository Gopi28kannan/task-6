n=[10,501,22,37,100,999,87,351]
a=[];b=[];c=[]
for j in n:
          a.clear()
          k=j
          while k!=1:
                    s=0
                    for i in str(k):
                              s=s+int(i)**2
                    if s not in a:
                           a.append(s)
                    else:
                              break
                    k=s
          if k==1:
                    b.append(j)
print("happy number = ",b)
