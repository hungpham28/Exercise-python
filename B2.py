#nhập vào 2 số 
#kiểm tra thử kiểu dữ liệu có phải số nguyên chưa
try:
    print("nhap vao so thu 1: ")
    so1=int(input())
    print("nhap vao so thu 2: ")
    so2=int(input())
    print("tong hai so la: ",so1+so2)
except:
    print("hai so nhap vao khong hop le: Eror type")