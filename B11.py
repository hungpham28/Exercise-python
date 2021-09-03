#Đọc file nhận giá trị tên và tuổi    
with open("Bai1.10.inp","r") as ifo:
    with open("Bai1.10.out","w") as rep:    
        try:
            name=ifo.readline().rstrip("\n")#Lấy tên từ file
            age=int(ifo.readline())#Lấy giá trị tuổi file
            rep.write(f"Vao 20 nam nua, tuoi cua {name} se la {age+20}") #Đưa ra file out
        except:
            rep.write("EROR: DATA TYPE ")#Đưa ra file out lỗi
    rep.close
ifo.close
