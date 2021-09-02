#nhap vao day so cach nhau bang khoang trang
strnumbers=input().split(sep=" ")
#chuyển day số từ dạng kí tự về số nguyên
numbers=map(int,strnumbers)
#tính tổng day số nhập vào
tong=sum(numbers)
#in ra màn hình tổng
print("Tong day so nhap vao la:",tong)