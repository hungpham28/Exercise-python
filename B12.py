#Đọc file lấy dữ liệu
with open("Bai1.12.inp","r",encoding="utf-8") as fi:
    lines=fi.read()#lấy toàn bộ dữ liệu vào
list_a_line=lines.splitlines()#dưa từng dòng thành dạng list
with open("Bai1.12.out","w",encoding="utf-8") as fo:
    fo.write(" ".join(list_a_line))#đưa ra file out các dòng trên 1 dòng cách nhau 1 khoảng trắng
fi.close
fo.close
   
    