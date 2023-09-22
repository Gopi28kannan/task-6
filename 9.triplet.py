def a(b,k):
          b.sort()
          c=[]
          for i in range(len(b)-2):
                    m=i+1
                    o=len(b)-1
                    while m<o:
                              if b[i]+b[m]+b[o]==k:
                                        c.append((b[i], b[m],b[o]))
                                        m+=1
                                        o-=1
                              elif b[i]+b[m]+b[o]<k:
                                        m+=1
                              else:
                                        o-=1
          return c
b = [10,20,30,9]
k = 59
print(a(b, k))
