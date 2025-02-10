#1
'''Yêu cầu: Cho người dùng nhập vào từ khóa cần tìm. Thực hiện đọc tập tin
san_pham.csv (được cung cấp theo đề) và xử lý tìm kiếm sản phẩm, nếu từ khóa
có xuất hiện trong tên sản phẩm hoặc mô tả sản phẩm thì in sản phẩm đó ra màn
hình như sau:

'''
import csv
with open('san_pham.csv', 'r', encoding='utf-8') as file: 
    nd = csv.reader(file)
    header = next(nd)
    kw = input('Nhập từ khoá cần tìm: ')
    found = [ i for i in nd if kw in i[1].lower() or kw in i[3].lower()]
print(f"TÌM THẤY {len(found)} SẢN PHẨM")
print("-"*70)
print("MÃ SP".ljust(12), "TÊN SẢN PHẨM".ljust(50), "GIÁ BÁN".ljust(10))
print("-"*70)
for i in found:
    print(f"SP{i[0].ljust(10)}", i[1].ljust(50), i[2].ljust(10))


# 
# 2
