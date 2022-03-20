def solve(arr):
    op = []
    for i in range(len(arr)):
        alpha = -1
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                alpha = arr[j]
                break 
        op.append(alpha)
    return op

def solve(arr):
    op = []
    stack = []
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            op.append(-1)
        elif stack[-1]<arr[i]:
            op.append(stack[-1])
        else:
            while len(stack)>0 and stack[-1]>arr[i]:
                stack.pop(-1)
            if len(stack)==0:
                op.append(-1)
            else:
                op.append(stack[-1])
        stack.append(arr[i])
    op.reverse()
    return op

arr = [1,3,2,4]
op = solve(arr)
print(op)