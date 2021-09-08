try:
    #nhap vao so nguyen n
    n=int(input())
    if 1<=n<=9:
        for i in range(n,0,-1):
            for j in range (i,0,-1):
                print(j,end=" ")
            print()
    else:
        print("nhap 1 so tu 1 den 9!")
except:
    print("dinh dang dau vao khong hop le")