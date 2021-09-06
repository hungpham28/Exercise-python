#Hàm xét 3 cạnh có phải là độ dài 3 cạnh tam giác
def kttg(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return False
    else:
        if abs(b-c)<a<b+c :
            return True
        else:
            return False
try:
    with open("bai22.inp","r") as fi:
        #nhập độ dài 3 cạnh tam giác từ bàn phím
        canh=fi.readline().rstrip("\n")
        #sắp xếp các cạnh tăng dần rồi bình phương
        canh=list(map(float,canh.split()))
        canh.sort()
        a,b,c=canh
        a2=a*a
        b2=b*b
        c2=c*c
        #xét tam giác đó là ta giác gì?
        if kttg(a,b,c):
            if a2+b2>c2:
                if a==b==c:
                    notify="tam giac deu"
                elif a==b:
                    notify="tam giac can"
                else:
                    notify="tam giac nhon"
            elif a2+b2<c2:
                notify="tam giac tu"
            else:
                if a==b:
                    notify="tam giac vuong can"
                else:
                    notify="tam giac vuong"
        else:
            notify="tam giac khong ton tai!"
#báo lỗi Eror
except FileNotFoundError:
    notify="Don't find file"
except:
    notify="DATA EROR"
#đưa ra kết quả
with open("bai22.out","w") as fo:
    fo.write(notify)
#-----------------------------------------------------------------------------------------------------------
# #Khoi lenh co the phat sinh loi
# try:
#    #Mo file voi mode='r' de doc file
#    with open('bai22.inp', 'r') as fileInp:
#        #Doc dong du lieu dau tien tu file
#        #Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
#        dongDauTien = fileInp.readline().rstrip('\n')

#    #Su dung ham map() va float de ep kieu du lieu sang so thuc
#    a, b, c = map(float, dongDauTien.split())

#    #Dung cau lenh re nhanh de kiem tra dieu kien cac tam giac
#    #Xu ly truong hop du lieu a, b, c am
#    if a<=0 or b<=0 or c<=0:
#        thongBao = "Cac canh cua tam giac phai lon hon 0!"
#    #Kiem tra dieu kien la ba canh cua tam giac
#    elif a+b>c and a+c>b and b+c>a:
#        #Kiem tra tam giac vuong
#        if a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b:
#            loaiTamGiac = 'vuong'
#        #Kiem tra tam giac deu
#        elif a==b and b==c:
#            loaiTamGiac = 'deu'
#        #Kiem tra tam giac can
#        elif a==b or a==c or b==c:
#            loaiTamGiac = 'can'
#        #Kiem tra tam giac tu
#        elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
#            loaiTamGiac = 'tu'
#        #Cac truong hop con lai la tam giac nhon
#        else:
#            loaiTamGiac = 'nhon'
#        #Thay doi thong bao theo yeu cau
#        thongBao = "{}, {}, {} la ba canh cua mot tam giac {}".format(a, b, c, loaiTamGiac)
#    else:
#        thongBao = "{}, {}, {} khong phai la ba canh cua mot tam giac".format(a, b, c)

# #Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
# except FileNotFoundError:
#    thongBao = "Khong tim thay file input!"

# #Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"
# except:
#    thongBao = "Dinh dang dau vao khong hop le!"

# #Mo file voi mode='w' de ghi file
# with open('bai22.out', 'w') as fileOut:
#    #Xuat thong bao ra file out
#    fileOut.write(thongBao)
