# list cho phép làm việc vs nhiều dữ liệu cùng lúc
#list có thể thay đổi giá trị của các phần tử trong nó
#create list
my_lst = [12,3.6,'test string',[8,9]]
print(my_lst)
print(type(my_lst))
# empty list
em_lst = [] 
em_lst_2 = list()
print(em_lst)
print(em_lst_2)

print(len(my_lst))
#truy cập từng phần tử list
#index dương
print(my_lst[1])
print(my_lst[-1])
#lấy khoảng 
print(my_lst[0:2])
# thay đổi giá trị
my_lst[0] = 20
print(my_lst)
print('test string' in my_lst)
for i in my_lst:
    print(i)

# nối list dùng + hoặc extend

my_lst_2 = ['li',123]
con_list = my_lst + my_lst_2
print(con_list)

# thêm với method append
# add .append() thêm vào cuối list
my_lst.append([9,10])
print("app",my_lst)
# extend
my_lst.extend(my_lst_2)
print(my_lst)
# sort list .sort() or sorted() phải cùng type, dùng hàm sorted() sẽ tạo ra hàm mới và hàm ban đầu không thay đổi
list_test = [1,30,22,44,12,90]
# list_test.sort()
# print(list_test)

list_sorted = sorted(list_test)
print(list_sorted)
# reverse list đảo ngược list
my_lst.reverse()
print(my_lst) 
# hoặc có thể dùng slicing
new_list = my_lst[::-1] #start:stop:step
print(new_list)
#insert element .insert(index, value)
my_lst.insert(0,'gia tri 1')
print(my_lst)
#delete element del or .remove(element)
del my_lst[1:4]
print(my_lst)

# trả về index đầu tiên của element được khớp .index() ko được phép có error
print(my_lst.index(20))

#pop(index)
ele = my_lst.pop(-1)
print(ele)
my_list = [1, 2, 3]  
my_list.extend([4, 5])  
print(my_list)