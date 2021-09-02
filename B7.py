#nhap vao hai so (exception handling)
try:
    so1=float(input())
    so2=int(input())
#in ra {so1} thap phan có {so2} chu so
    print('{0:.{1}f}'.format(so1,so2),"Done!")
except:
    print("Eror: data type")