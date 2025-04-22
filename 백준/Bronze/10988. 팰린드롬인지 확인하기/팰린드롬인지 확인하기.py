sen = input()
arr = []
for i in range(0, len(sen)):
    arr.append(sen[i])

checker = arr.copy()
arr.reverse()


if(arr == checker):
    print("1")
else:
    print("0")

