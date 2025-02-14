#xử lý ngoại lệ là gì: tránh TH chương trình bị ngắt khi chạy mà gặp lỗi crash, giúp xác định và quản lý lỗi cụ thể, thông tin cụ thể
# 4 key chính
# # try:
#     run this code
# # except:
#     excute this code when there is an Exception
# # else:
#     no Exception -> run this code
# # finally:
#     always run this code

#example
# my_dict = {'age':10,'name':"zed"}
# try:
#     result = 10 / 0
#     my_val = my_dict['name']
# except:
#     print("all loi xay ra deu vao except")
# print('het chuong trinh')

#example lỗi cụ thể có thể cho vào từng except
my_dict = {'age':10,'name':"zed"}
try:
    # result = 10 / 0
    my_val = my_dict['add']
except ZeroDivisionError:
    print("loi chia cho 0")
except KeyError:
    print("key khong dung")  
print('het chuong trinh')