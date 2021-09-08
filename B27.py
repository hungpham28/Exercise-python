try:
    n=int(input())
    if 0<n<10:
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
    else:
        print(f"bang cuu chuong khong co {n}")
except:
    print("du lieu khong phu hop")