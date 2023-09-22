from collections import*
a=[1,2,3,4,1,2,67]
b=[]
s=Counter(a)
for i in s:
          if s[i]>1:
                    pass
          else:
                    b.append(i)
print('non repeating elements : ',b)
