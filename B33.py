
#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    x = float(input())
    n = int(input())
    tong=1#gán cho tổng bằng 1
    giaithua=1#gán phép nhan tich
    if n>=0:#n phải là số tự nhiên
        #cho vòng chạy từ 0 đến n và ta sẽ được phép tính 
        for i in range(1,2*n+1):
            giaithua*=i
            if i % 2==0: #nếu là chẵn ta thực hiện phép +
                tong+=(x**i)/giaithua
            else:#nếu lẻ ta thực hiện phép -
                tong-=(x**i)/giaithua
        print('{:.5f}'.format(tong))
    else:
        #nếu không phải là số tự nhiên thì thông báo
        print("nhap vao so tu nhien !")
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")