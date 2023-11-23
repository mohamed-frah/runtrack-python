pre = [1, 2, 3, 4, 5]
print(pre)
x = pre[4]
pre[4] = pre[0] 
pre[0] = x
print(pre)