#tuple có tốc độ xử lý lớn hơn list, vì nó immutable thường dùng để lưu trữ các giá trị cố định không thay đổi
#tạo tuple
tuple_1 = ('a',3) #không được tạo như thế này tuple_1 = ('a') vì vậy sẽ được hiểu  là str, phải thêm dấu phẩy , đằng sau nếu chỉ có 1 phần tử
tuple_2 = ('b',)
print(tuple_1)
print(type(tuple_1))

# duyệt qua các phần tử của tuple

tuple_3 = ('a',1,2,3,32)
tuple_4 = ('a',1,2,3,32)
print('chiều dài của tuple 3 là : ', len(tuple_3))
for i in tuple_3:
    print(i)

print(tuple_3[2])

# cộng các tuple
new_tuple = tuple_1 + tuple_3
print(f"new tuple : {new_tuple}")
#conver qua list để thao tác thêm xóa và conver ngược lại để sử dụng tuple
list_1 = list(new_tuple)
#add thêm phần tử
list_1.append('test')

#xóa phần tử
list_1.remove(32)
#conver về tuple
new_tuple = tuple(list_1)
print(new_tuple)

#method đếm số lần xuất hiện trong 1 tuple

print(new_tuple.count(1))

# trích xuất index theo phần tử
print(new_tuple.index(1))

# id của tuple khác list, list là khác nhau tuple giống nhau
print(f"ID of tuple 3 : {id(tuple_3)}")
print(f"ID of tuple 4 : {id(tuple_4)}")
# muốn thay đổi phần tử phải vào đúng vị trí và type ví dụ tuple_5[0][0] là list
tuple_5 = ([1,2,3],'a',7,8,'b')
tuple_5[0][0] = 10
print(tuple_5) #([10, 2, 3], 'a', 7, 8, 'b')
my_tuple = (1, 2, 3)   