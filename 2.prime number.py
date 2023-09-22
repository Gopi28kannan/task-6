n=[10,501,22,37,100,999,87,351]
print("input = ",n)
a=[];b=[]
n1=len(n)
for i in n:
          c=0
          for j in range(2,i):
                    if (i%j)==0:
                              c=1
          if c==0 and i>1:
                    a.append(i)
print('prime number = ',a)
