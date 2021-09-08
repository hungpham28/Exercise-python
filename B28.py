try:
    #nhap vao 2 so a,b
    a=int(input())
    b=int(input())
    #biến chạy đầu tiên
    if a>b:#chỉ xét a<b
        print("so thu 1 phai nho hon so thu 2")
    else:    
        dem=0
        for i in range(a,b):
            if i%5==0:
                #biến đếm số thứ n chia hết cho 5
                dem+=1
                #nếu quá 11 số thì thoát vòng for
                if dem==11:
                    break
                else:
                    #nếu chưa quá 10 thì in ra tiếp
                    print(i,end=" ")
        #Thông báo phù hợp
        if dem==0:
            print("khong co so nao chia het cho 5")
        elif dem<=10:
            print("\nDa in het cac so chia het cho 5")
        else:
            print("\nIn qua 10 so roi!")
except:#kiểu dữ liệu vào phải hợp lệ là số nguyên
    print("dau vao khong hop le!")