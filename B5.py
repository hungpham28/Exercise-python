#nhap vao so thap phan va kiem tra kieu du liệu có hợp lệ ko
try:
    print("moi nhap vao so thap phan:")
    so_10=int(input())
    print("so thap phan %d chuyen sang bat phan la: %o" %(so_10,so_10))
except:
    print("erordata input ")
print("khong can sua doi")
