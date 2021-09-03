#nhập tên, tuổi từ file "  "
with open("Bai1.10.inp","r") as ifo:
    name=ifo.readline().rstrip("\n")
    age=int(ifo.readline())
with open("Bai1.10.out","w") as reply:
    reply.write(f"Vao 20 nam nua, tuoi cua {name} se la {age+20}")
ifo.close
reply.close
