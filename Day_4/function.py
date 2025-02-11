## function in py 
# sử dụng nhiều lần mà k cần viết lại
# def my_sum(x,y):
#     return x + y
# print(sum(23,4))

import shutil
import os
# coppy file a và b tại source_dir qua des_dir
def coppy_file_func(source_dir,des_dir):
    
    list_name = os.listdir(source_dir)

    for file_name in list_name:
        shutil.copy(os.path.join(source_dir,file_name),os.path.join(des_dir,file_name))

source = r"D:\A_Python_30Day\Day_4\source_dir"
des = r"D:\A_Python_30Day\Day_4\des_dir"


coppy_file_func(source,des)
def display_info(name, age):  
    print(f"Name: {name}, Age: {age}")  
 
display_info(age=25, name="Alice")  