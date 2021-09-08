try:
    #nhap 2 số 2 a,b
    a=int(input())
    b=int(input())
    sum=0
    #nếu a<=b
    if a<=b:
        for i in range(a,b+1):
            sum+=i
    else:
        #nếu a>b thì nhập lại
        print("a lon hon b ?")
    print("tong cac so nguyen tu a den b: ",sum)
except:
    print("Data eror")