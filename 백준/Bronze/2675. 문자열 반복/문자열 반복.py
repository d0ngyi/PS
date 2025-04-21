t = int(input())

for i in range(0, t):
    ans = ""
    case = input()
    r, s = case.split()
    r = int(r)
    for j in range(0, len(s)):
        ans += s[j] * r
    print(ans)