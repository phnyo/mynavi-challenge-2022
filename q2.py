s = 'なんじ、ぶんがくとかがくのちからをしんじよ'
t = 'じょうほうぶんせきしてかいぜんあくしょん'

dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]

for i in range(len(t)):
    for j in range(len(s)):
        if s[j] == t[i]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

res = ''

j = len(s)
i = len(t)
while True:
    while j > 0 and dp[i][j] == dp[i][j - 1]:
        j = j - 1
    while i > 0 and dp[i][j] == dp[i - 1][j]:
        i = i - 1
    if i <= 0 or j <= 0:
        break
    res += s[j - 1]
    i = i - 1
    j = j - 1
print(res[::-1])
