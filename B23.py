import math
with open("bai23.out","w",encoding="utf-8") as fo:
    try:         
        #đọc file input
        with open("bai23.inp","r") as fi:
                option=float(fi.readline().rstrip("\n"))
                if option==1:
                    #lựa chọn 1 giải phương trình bậc nhất
                    a,b=map(float,fi.readline().rstrip("\n").split())
                    if a==0:
                        if b==0:
                            fo.write("phương trình có vô số nghiệm")
                        else:
                            fo.write("phương trình vô nghiệm")
                    else:
                        x=-b/a
                        fo.write(f"phương trình có nghiệm duy nhất x={x}")
                elif option==2:
                    #lựa chọn 2 giải phương trình bậc hai
                    a,b,c=map(float,fi.readline().rstrip("\n").split())
                    delta=b*b-4*a*c
                    if delta<0:
                        fo.write("phương trình vô nghiệm")
                    elif delta==0:
                        x=-b/(2*a)
                        fo.write(f"phương trình có nghiệm kép x1=x2={x}")
                    else:
                        fo.write("phương trình có 2 nghiệm phân biệt \n")
                        x1=(-b-math.sqrt(delta))/(2*a)
                        x2=(-b+math.sqrt(delta))/(2*a)
                        fo.write(f"  x1={x1}")
                        fo.write(f"\n  x2={x2}")
                else:
                    #nếu nằm ngoài lựa chọn 1 2 thì mời chọn lại
                    fo.write("Vui long chon mot trong hai chuc nang:\n")
                    fo.write("  1. Giai phuong trinh bac nhat\n")
                    fo.write("  2. Giai phuong trinh bac hai\n")
        fi.close()
    #Thông báo lỗi
    except FileNotFoundError:
            fo.write("Khong tim thay file input!")
    except:
            fo.write("EROR DATA INPUT")
fo.close()