# KeyError truy cập vào key không có trong 1 dictionary thì sẽ báo lỗi
# my_dict = {"name":'zed',"age":18}
# print(my_dict['address'])  #KeyError: 'address' không có key address


# TypeError sai kiểu dữ liệu (số + string = error)
# str = "thanh zed 2k" + 123
# print(str) #TypeError: can only concatenate str (not "int") to str



# ImportError khi import 1 module của thư viện mà module đó không tồn tại trong thư viện đó sẽ báo lỗi
# from numpy import my_module  #ImportError: cannot import name 'my_module' from 'numpy' (D:\A_Python_30Day\my_env\Lib\site-packages\numpy\__init__.py)


# ValueError khi dùng đúng kiểu dữ liệu tuy nhiên giá trị không hợp lệ (str "abc" chuyển thành số  = error)
# str = "thanhzed2k"
# num = int(str)
# print(num) #ValueError: invalid literal for int() with base 10: 'thanhzed2k'


# ZeroDivisionError không thể chia cho 0
# print(100 / 0) #ZeroDivisionError: division by zero