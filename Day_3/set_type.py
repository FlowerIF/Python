# tạo set
my_set = {'a','b'}
print(my_set)
print(type(my_set))
# tạo set rỗng
# my_set = set()
# print(type(my_set))

# set không cho phép các phần tử lặp lại
my_set_1 = {'a','b','a'}
print(my_set_1)

#check set là unorder (mỗi lần chạy lại thì thứ tự kết quả sẽ khác nhau)
my_set_2 = {'a','b','c','d'}
for i in my_set_2:
    print(i)
# update set(hay sử dụng thêm vào set)
my_set_3 = {'a','b','c','d'}
my_set_3.add('e')
print(my_set_3)
#xóa
my_set_3.discard('a')
print(my_set_3)

# thao tác với 2 hay nhiều sét, xem thêm sơ đồ venn( giao, hợp, riêng )
my_set_3 = {'a','b','c','d'}
my_set_4 = {'a','g','d','k'}
#giao intersection
inter_set = my_set_3.intersection(my_set_4) 
print(f'inter set 3,4 : {inter_set}')
#hợp union
union_set = my_set_4.union(my_set_3)
print(f'inter set 3,4 : {union_set}')
#riêng symetric_difference
symetricdifference_set = my_set_4.symmetric_difference(my_set_3)
print(f'symmetric_difference set 3,4 : {symetricdifference_set}')