from os import write
#Hàm xét 3 cạnh có phải là độ dài 3 cạnh tam giác
def kttg(a,b,c):
    if abs(b-c)<a<b+c :
        return True
    else:
        return False
try:
    with open("bai20.inp","a") as fi:
        #nhập độ dài 3 cạnh tam giác từ bàn phím
        canh=list(map(float,fi.readline().strip("\n").split()))
        #sắp xếp các cạnh tăng dần rồi bình phương
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
with open("bai20.out","w") as fo:
    fo.write(notify)
