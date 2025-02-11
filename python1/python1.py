#1
'''Yêu cầu: Cho người dùng nhập vào từ khóa cần tìm. Thực hiện đọc tập tin
san_pham.csv (được cung cấp theo đề) và xử lý tìm kiếm sản phẩm, nếu từ khóa
có xuất hiện trong tên sản phẩm hoặc mô tả sản phẩm thì in sản phẩm đó ra màn
hình như sau:

'''
# import csv
# with open('san_pham.csv', 'r', encoding='utf-8') as file: 
#     nd = csv.reader(file)
#     header = next(nd)
#     kw = input('Nhập từ khoá cần tìm: ')
#     found = [ i for i in nd if kw in i[1].lower() or kw in i[3].lower()]
# print(f"TÌM THẤY {len(found)} SẢN PHẨM")
# print("-"*70)
# print("MÃ SP".ljust(12), "TÊN SẢN PHẨM".ljust(50), "GIÁ BÁN".ljust(10))
# print("-"*70)
# for i in found:
#     print(f"SP{i[0].ljust(10)}", i[1].ljust(50), i[2].ljust(10))



# 2

'''Yêu cầu: Đọc tập tin python.txt (được cung cấp theo đề) và thực hiện đếm số lần
xuất hiện của các từ trong tập tin.'''

# with open('python.txt', 'r', encoding='utf-8') as file:
#     nd = file.read()
# nd_clean = nd.replace(".", "").replace(",", "")
# nd_list = nd_clean.split(" ")
# print("TỪ".ljust(10), "SỐ LẦN".rjust(10))
# print("-"*30)
# for i in  set(nd_list):
#     count = nd_list.count(i)
#     print(f"{i}".ljust(20), f"{count}".ljust(20))



# 3
'''Yêu cầu: Cho người dùng nhập vào 1 chuỗi mật khẩu, kiểm tra độ mạnh của mật
khẩu theo các tiêu chí sau:
o Mật khẩu phải có:
▪ Ít nhất 8 ký tự.
▪ Có chứa ít nhất 1 ký tự chữ hoa (upper).
▪ Có chứa ít nhất 1 ký tự đặc biệt (!, @, #, $, %, &)
▪ Có chứa ít nhất 1 ký tự số (từ 1 đến 9).'''

# import re
# pw = input ("Nhập mật khẩu: ")
# errors = []
# if len(pw) < 8: 
#     errors.append("- Mật khẩu phải có ít nhất 8 ký tự")

# if not re.search(r"[A-Z]",pw):
#     errors.append("- Mật khẩu phải có chứa ít nhất 1 ký tự chữ hoa (upper)")

# if not re.search(r"[!@#$%&]", pw):
#     errors.append("- Mật khẩu phải có chứa ít nhất 1 ký tự đặc biệt (!, @, #, $, %, &)")
#     # Mật khẩu phải có chứa ít nhất 1 ký tự số (từ 1 đến 9)"

# if not re.search(r"[1-9]", pw): 
#     errors.append("- Mật khẩu phải có chứa ít nhất 1 ký tự số (từ 1 đến 9)")
# if errors:
#     print("Mật khẩu chưa đạt yêu cầu.")
#     print("\n".join(errors))
# else:
#     print("Mật khẩu đạt yêu cầu")


#4
'''Cho danh sách nhân viên. Hãy thực hiện các yêu cầu sau

c.Tạo cột dữ liệu mới là Increase_Salary. Dữ liệu là Yes nếu nhân viên có tăng
ca, ngược lại thì Increase_Salary là No

d. Xuất kết quả sau khi tính toán ra tập tin nhan_su_2.csv
'''

'''a. Cập nhật tiền lương cho các nhân viên bị thiếu (cột tiền lương đang có dấu ?).
Biết rằng các nhân viên cùng phòng sẽ có mức lương bằng nhau.'''

import pandas as pd
df = pd.read_csv('nhan_su.csv', na_values=['?'])
# salary_by_dept = df.groupby("Dept")['Salary'].transform('mean')

# df["Salary"].fillna(salary_by_dept, inplace=True)
# df.to_csv('nhan_su.csv', index=False)
# print(df)

# b

'''b. Tính thêm 10% tiền lương cho nhân viên có tăng ca (cột Overtime bằng 1). Cập
nhật lại giá trị tiền lương trong cột Salary cho nhân viên.'''

overtime_employee = df[df["Overtime"] == 1]
# overtime_employee["Salary"] = overtime_employee["Salary"]*1.1
# df.update(overtime_employee)
# df.to_csv('nhan_su.csv', index=False)
# print(df)


increased_salary = df["Overtime"].apply(lambda x: "Yes" if x == 1  else "No")
df["Increased_Salary"] = increased_salary
df.to_csv('nhan_su.csv', index=False)
print(df)
