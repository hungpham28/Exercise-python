#viết thêm exception handling
#Nhap vào day so cach nhau bằng khoảng trắng
try:
    strnumbers=input().split(sep=" ")
    numbers=map(int,strnumbers)
    #in ra man hình tổng dãy số nhập vào
    print("Tong day so la:",sum(numbers))
except:
    #in ra thông báo lỗi
    print("EROR: DATA TYPE")