#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())
    #số nhập vào là số tự nhiên nếu không in ra thông báo
    if n>=0:
        #mã ASCII chữ cái đầu "A"là 65
        maASCII=65
        #Số khoảng trắng bắt đầu
        space_start=n
        #sếp chồng kim tự tháp
        for i in range(1,n+1):#vòng for chạy từng dòng
            print("  "*(space_start-i),end="")#bắt đầu mỗi dòng là 2 khoảng trắng*công thức
            for j in range(1,2*i):
                print(chr(maASCII),end=" ")#bắt ghi ra kí tự theo mã ASCII và mỗi khoảng trắng
                maASCII+=1#tăng mã ASCII
                if maASCII>90:#nếu mã nằm ngoài kí tự chữ cái thì về lại kí tự đầu là A
                    maASCII=65
            print()
    else:
        #nếu không phải là số tự nhiên thì thông báo
        print("nhap vao so tu nhien !")
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")