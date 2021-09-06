import math
#nhập vào hệ số a,b,c của phương trình bậc 2 ax^2+bx+c
a,b,c=map(float,input("nhap he so a,b,c ax^2+bx+c: ").split())
#xét hệ số a=0 và a!=0
if a==0:
    #in phương trình có 1 nghiệm duy nhất
    try:
        x=-c/b
        print(f"phuong trinh co nghiem duy nhat x={x}")
    except:
        print("phuong trinh co vo so nghiem")
else:
    #xet delta và số nghiệm của phương trình bậc 2 a!=0
    delta=b*b-4*a*c
    if delta<0:
        print("phuong trinh vo nghiem")
    elif delta==0:
        x=-b/(2*a)
        print(f"phuong trinh co nghiem kep x1=x2={x}")
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(b-math.sqrt(delta))/(2*a)
        print(f"phuong trinh co 2 nghiem x1={x1} va x2={x2}")
