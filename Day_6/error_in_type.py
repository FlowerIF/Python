# SyntaxError cú pháp sai
# print 'syntax error' #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# if True
#     print("it's true")

# NameError tên đặt không đúng hoặc chưa được định nghĩa
# print(my_err) #NameError: name 'my_err' is not defined

# IndexError index vượt ngoài phạm vi cho phép
# my_list = [1,2,3,4]
# print(my_list[9]) IndexError: list index out of range


# ModuleNotFoundError chưa cài đặt module mà đã khai báo thì sẽ lỗi
# import numpy as np
# my_arr = np.array([1,2,3,4])
# print(my_arr) #ModuleNotFoundError: No module named 'numpy'


# AttributeError sử dụng method không đúng của type dữ liệu đó sẽ báo lỗi

# my_str = "it's true"
# print(my_str.append("error")) #AttributeError: 'str' object has no attribute 'append'