#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    n = input()
    if int(n)<0:#nếu n<0 thì thông báo
        print("nhap vao so tu nhien!")
    else:
        #khởi tạo chẳn lẻ bằng 0
        chan=0
        le=0
        #ta chạy vòng for dưới dạng chuỗi mỗi kí tự là 1 chữ số
        for i in n:
            sothu_i=int(i)#đưa kí tự về số
            if sothu_i % 2==0:#nếu là số chẵn
                chan+=sothu_i
            else:#nếu là số lẻ
                le+=sothu_i
        print(le*chan)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")