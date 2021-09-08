try:
    n=int(input())
    if 1<=n<=9:
        #sắp xếp vòng for sếp chồng
        for i in range(1,n+1):
            for j in range(1,i+1):
                if j==i:
                    print(j)
                else:
                    print(j,end=" ")
    else:
        print("nhap 1 so trong khoang tu 1 den 9!")
except:#thông báo lỗi đầu vào 
    print("dinh dang dau vao ko hop le!")