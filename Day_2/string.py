#string chuoi các ký tự, character không được hỗ trợ kiểu trong py mà nó đơn giản là string có chiều dài = 1

# để xuống dòng có thể sử dụng """vvv""" hoặc '''xx'''

my_str = 'test string'
print(my_str)

my_str_line = '''test
line 2'''
print(my_str_line)
#chieu dai chuoi
print(len(my_str_line))
# truy cập tới ký tự cần tìm index
# index dương được đánh từ 0 -> len(str) - 1
print(my_str_line[len(my_str_line)-1])
# index âm chạy từ -len(str) -> -1
print(my_str_line[-len(my_str_line)])
#slicing for string lấy khoảng các ký tự
print(my_str_line[0:2]) #lấy ký tự có index từ 0 đến 1
#my_str_line[:-1] # không bao gồm index -1
# nối chuỗi
str_1 = 'test '
str_2 = 'noi'
str = str_1+ str_2
print(str)
for i in str:
    print(i)
# kiểm tra chuỗi con có trong chuỗi cha không?

str_con = '12'
if str_con in str:
    print('yes')
else:
    print('no')

#methods
#viết hoa
print(str.upper())
#in thường
print(str.lower())

#string is immutable in python không thể thay đổi các ký tự trong string

print('no' in str)
