def armstrong():
    for elm in range(1,1001):
        n = elm
        b = str(elm)
        length = len(b)
        sum = 0
        for el in b:
            sum=sum+int(el)**length
        if sum == n:
            print(n,"is armstrong number")
armstrong() 
