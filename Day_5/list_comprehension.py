# cung cấp cú pháp ngắn hơn từ giá trị list đã có sẵn
#[expression for item in iterable]  expression là phép toán


# tạo list ban đầu thông thường
l = [1,2,3,4,5]
new_lst = []
for x in l:
    new_lst.append(x**2)
print(new_lst)

# mới list comprehension

new_com_lst = [(x ** 2) for x in l] #duyệt từng phần tử trong list cũ với phép toán là các phần tử bình phương
print(new_com_lst)

#lọc các phần tử số lẻ
#[expression for item in iterable if condition  == True]
so_le = [ x for x in l if x % 2 == 1]
print(so_le)

# apply funct cho tất cả các phần tử
#[expression_1 if condition == True else expression_2 for item in iterable]
#nếu là số lẻ thì + thêm 2, số chẵn giữ nguyên
new_ex = [x if (x % 2 == 0) else (x + 2) for x in l]
print(new_ex)

# dictionary comprehension và set comprehension

# dict sử dụng {key:value for item in iterable}
new_dict = {k:k ** 2 for k in l}
print(new_dict)

#SET
#{item for item in iterable}
str = "DOHOAI"
new_set = {i for i in str} # lấy các giá trị tồn tại 1 lần ( tính chất của set )
print(new_set)