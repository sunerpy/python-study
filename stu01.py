# 9*9 
m = 1
n = 1
while n<10 :
    while m <= n :
        num = m * n
        print(m,"*",n,"=",num,sep='',end='\t')
        m += 1
    m = 1
    n += 1
    print()