try:
    #nhap 2 số 2 a,b
    a=int(input())
    b=int(input())
    sum=0
    i=a
    #nếu a<=b
    if a<=b:
        while a<=i<=b:
            sum+=i
            i+=1
    else:
        #nếu a>b thì nhập lại
        print("a lon hon b ?")
    print("tong cac so nguyen tu a den b: ",sum)
except:
    print("Data eror")