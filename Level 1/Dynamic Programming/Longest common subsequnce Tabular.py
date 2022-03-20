def lcs(x,y,n,m):
    dp = []
    for i in range(n+1):
        row = []
        for j in range(m+1):
            if i==0 or j==0:
                row.append(0)
            else:
                row.append(-1)
        dp.append(row)

    for i in dp:
        print(*i)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

    for i in dp:
        print(*i)

    return dp[-1][-1]
   
x = "abcde"
y = "ace"
n = len(x)
m = len(y)
length = lcs(x,y,n,m)
print(length)