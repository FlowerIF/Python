#function open(filename,mode)
# 4 mode
# "r" read, trả về lỗi nếu không có file đó tồn tại
# "a" append
# "w" viết, tạo nếu  File không tồn tại
# "x" tạo, trả về lỗi nếu file không tồn tại
# xử lý file dưới 2 dạng binary hoặc text mode
# "t" text là dữ liệu mặc định. text mode 
# "b" binary mode

#đọc file
# file_open = open(r"Day_5\text.txt","r") 
# content = file_open.read()
# print(content)
# file_open.close

# hoặc có thể sử dụng context manage để mở file, sử dụng nó không cần phải đóng file thủ công cách này hay sử dụng nhất
with open(r"Day_5\text.txt") as file_open:
    content = file_open.read() #có thể sử dụng đọc các dòng .readline() ,readlines()
    print(content)

#Ghi file mới

with open(r"Day_5\new_file.txt","w") as file_crea:
    file_crea.write("day la dong text")

#ghi thêm nội dung vào file cũ đã có
with open(r"Day_5\new_file.txt","a") as file_crea:
    file_crea.write("\nday la text da them sau do")

#"x" tạo file mới không cần thêm nội dung
with open(r"Day_5\new_file_x.txt","x") as f:
    pass