n = int(input())
arr = list(map(int, input().split(" ")))
stack = []
count = 1
checker = True
while len(arr) != 0 or len(stack) != 0:
    if len(arr) > 0 and arr[0] == count:
        del arr[0]
        count += 1
    elif len(stack) > 0 and stack[len(stack) - 1] == count:
        stack.pop()
        count += 1
    elif len(arr) > 0:
        b = arr[0]
        del arr[0]
        stack.append(b)
    else:
        break


if len(arr) == 0 and len(stack) == 0:
    print("Nice")
else:
    print("Sad")