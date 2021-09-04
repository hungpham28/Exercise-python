#nhập vào độ dài 3 cạnh của tam giác lần lượt là a,b,c
a,b,c=int(input("nhap lan luot do dai 3 canh tam giac:").split())
#xet dieu kien thoa man cua 1 tam giac    
    if abs(b-c)<a and a<b+c:
        print("do dai 3 canh ton tai 1 tam giac:")
    else:
        print("khong ton tai tam giac:")
