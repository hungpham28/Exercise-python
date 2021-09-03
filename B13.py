try:    
    with open("Bai1.12.inp","w") as fi:
        lines=fi.read()
    list_a_line=lines.splitlines()
    with open("Bai1.12.out","w") as fo:
        fo.write(" ".join(list_a_line))
except:
    with open("Bai1.12.out","w") as fo:
        fo.write("Don't find file input")
fi.close
fo.close