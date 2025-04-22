total = 0
ans = 0

for i in range(0,20):
    info = input()
    sub, num, grade = info.split(" ")
    num = float(num)
    if(grade == "A+"):
        ans += 4.5 * num
        total += num
    elif grade == "A0":
        ans += 4 * num
        total += num
    elif grade == "B+":
        ans += 3.5 * num
        total += num
    elif grade == "B0":
        ans += 3 * num
        total += num
    elif grade == "C+":
        ans += 2.5 * num
        total += num
    elif grade == "C0":
        ans += 2 * num
        total += num
    elif grade == "D+":
        ans += 1.5 * num
        total += num
    elif grade == "D0":
        ans += 1 * num
        total += num
    elif grade == "F":
        ans += 0 * num
        total += num
    else:
        continue

print("{:.6f}".format(ans/total))