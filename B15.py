try:# exception handling
    # nhập tên và chiều cao người thứ nhất trên 1 dòng
    while True:
        name1,high1=input("Enter the name and height of people 1:").split()
        high1=int(high1)
        if high1<=0:
            print("height must be a positive number")
        else:
            break
    # nhập tên và chiều cao người thứ hai trên 1 dòng
    while True:
        name2,high2=input("Enter the name and height of people 2:").split()
        high2=int(high2)
        if high2<=0:
            print("height must be a positive number")
        else:
            break
    if high1<0 or high2<0:
        print("height can't be nagative")
    #so sánh chiều cao hai bạn
    if high1>high2:
        print(f"{name1} cao hon {name2}")
    elif high1<high2:
        print(f"{name2} cao hon {name1}")
    else:
        print(f"{name1} va {name2} cao bang nhau")
except:
    #in ra màn hình nếu dữ liệu đầu vào ko hợp lệ
    print("EROR:Data type \n Enter the name and height of each person on a line one at a time\nThe letters and numbers are separated by a space")