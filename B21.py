#Hàm xét 3 cạnh có phải là độ dài 3 cạnh tam giác
def kttg(a,b,c):
    if abs(b-c)<a<b+c :
        return True
    else:
        return False
#nhập độ dài 3 cạnh tam giác từ bàn phím
canh=list(map(float,input("nhap do dai 3 canh tam giac: ").split()))
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
            print("tam giac deu")
        elif a==b:
            print("tam giac can")
        else:
            print("tam giac nhon")
    elif a2+b2<c2:
        print("tam giac tu")
    else:
        if a==b:
            print("tam giac vuong can")
        else:
            print("tam giac vuong")
else:
    print("tam giac khong ton tai!")