#Nhap so A tu ban phim va chuyen sang kieu so thuc
soA = float(input())

#Nhap so B tu ban phim va chuyen sang kieu so nguyen
soB = int(input())

#Dung ham format de dinh dang chuoi dau ra
print('{1:.{0}f} va {2}'.format(soB, soA, str(soA)))
# phân tích câu lệnh
# print('{1:.{0}f} va {2}'.format(soB, soA, str(soA)))
# các biến soB, soA, str(soA) sẽ lần lượt gán theo thứ tự 0,1,2 