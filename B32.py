#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    #khởi tạo giai thừa gán bằng 1
    giaithua=1
    #số nhập vào là số tự nhiên nếu không in ra thông báo
    if n>=0:
        #dùng vòng for với biến chạy là i và giaithua nhân i
        for i in range(1,n+1):
            giaithua*=i
        print(n,"! = ",giaithua,sep="")
    else:
        #nếu không phải là số tự nhiên thì thông báo
        print("nhap vao so tu nhien !")
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")