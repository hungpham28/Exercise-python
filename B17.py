#exception handling from B16.py
try:
    a,b,c=map(int,input("nhap vao 3 do dai 3 canh cua tam giac:").split())
    if abs(b-c)<a<b+c:
        print("ton tai tam giac")
    else :
        print("Khong ton tai tam giac")
except:
    print("Eror:Data Type")