ls = [[0,'M',0,'M',0],
      [0,0,'M',0,0],
      [0,0,0,0,0],
      ['M','M',0,0,0]]


def foo(ls):
    m = len(ls)
    n = len(ls[0])
    ls1 = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 'M':
                ls1[i][j] = 'M'
            else:
                count = 0
                for k in range(-1,2):
                    for l in range(-1,2):
                        if k == 0 and l ==0:
                            continue
                        x = k + i
                        y = l + j
                        if 0 <= x < m and 0 <= y < n and ls[x][y] == 'M':
                            count += 1
                ls1[i][j] = count
    return ls1                        

new = foo(ls)
for i in new:
    print(i)

