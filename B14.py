#Hàm đưa 1 dòng string gồm string và value trả về 2 giá trị string và value riêng biệt  
def covert_type(typelist):
    return typelist[0],int(typelist[1])
#Mở đọc file 
with open("Bai1.14.inp","r") as fi:
    #Đọc dòng 1 và đưa về list các phần tử cách nhau khoảng trắng
    line1=fi.readline().strip("\n").split(sep=" ")
    #Nhận giá trị từ hàm Covert_type
    name1,high1 = covert_type(line1)
    #Đọc dòng 1 và đưa về list các phần tử cách nhau khoảng trắng
    line2=fi.readline().strip("\n").split(sep=" ")
    #Nhận giá trị từ hàm Covert_type
    name2,high2 = covert_type(line2)
#Ghi file
with open("Bai1.14.out","w") as fo:
    #so sánh 2 giá trị high1 và high2 ai cao hơn thì xuất ra file out
    if high1>high2:
        fo.write(f"{name1} cao hon {name2}")
    elif high1<high2:
        fo.write(f"{name2} cao hon {name1}")
    else:
        fo.write(f"{name2} va {name1} cao bang nhau")
fi.close
fo.close

