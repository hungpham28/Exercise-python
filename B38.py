#function tìm ước số và trả về dạng list
def uocso(a):
    list_uocso=[]
    for i in range(1,a+1):
        if a % i==0:
            list_uocso.append(i)
    return list_uocso
#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    n = int(input())
    if int(n)<0:#nếu n<0 thì thông báo
        print("nhap vao so tu nhien!")
    else:
        if sum(uocso(n))-n==n: #nếu tổng ước số = chính nó thì là số hoàn hảo
            print(n," la so hoan hao :)")
        else:
            print(n," khong la so hoan hao :(")
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")