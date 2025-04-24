while 1:
    info = list(input())
    if(len(info) == 1 and info[0] == "."):
        break
    arr = []
    for i in info:
        if(i == "(" or i == ")" or i == '[' or i == "]"):
            arr.append(i)
    stack = []
    checker = True
    for i in arr:
        if i == "(" or i == "[":
            stack.append(i)
        elif len(stack) != 0 and i == ")" and stack[-1] == "(" :
            stack.pop()
        elif len(stack) != 0 and i == "]" and stack[-1] == "[":
            stack.pop()
        else:
            checker = False
            break
    
    if len(stack) == 0 and checker:
        print("yes")
    else:
        print("no")
        