
#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    n = int(input())
    if n<0:#nếu n<0 thì thông báo
        print("nhap vao so tu nhien!")
    else:
        cs=1
        #tìm số chữ số của n và cs=10^số chữ số
        while cs<n:
            cs*=10
        #cs phải nhỏ hơn n
        daonguoc=0
        while cs!=1:#chạy đến khi cs=1
            cs//=10#giảm cs xuống 1 chữ số khi chạy
            csthu_k=n % 10 #lấy chữ số cuối của n
            n //= 10#lấy các chữ số còn lại của n
            daonguoc+=csthu_k*cs#lấy chữ số cuối lên đầu
        print(daonguoc)#in ra kết quả cuôi cùng
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")