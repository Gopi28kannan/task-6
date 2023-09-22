def a(n, m):
          r = 1
          if m > n - m:
                  m = n - m
          for i in range(0, m):
                    r *= (n - i)
                    r /= (i + 1)
          return r
def b(m, n):  
          if m<n:
                    return 0
          c = a(n + m-1, n-1)
          return int(c)
if __name__ == '__main__':
          m = 13; n = 6
 
result = b(m, n)
print(result)
