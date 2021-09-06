#nhap vao 1 dong gồm số các phép tính ví dụ 4 + 5
so1,pheptinh,so2=input().split()
#đưa về số thực
so1=float(so1)
so2=float(so2)
#lưu kết quả khi chưa có
result=None
#Xác định phép tính +,-,*,/ để thực hiện
if pheptinh=="+":
    result=so1+so2
elif pheptinh=="-":
    result=so1-so2
elif pheptinh=="*":
    result=so1*so2
elif pheptinh==":":
    if so2==0:
        print("so bi chia phai khac 0!")
    else:
        result=so1/so2
#xem thử kết quả có hợp lệ
if result != None:
    print(f"{so1} {pheptinh} {so2} = {result}")
