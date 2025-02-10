# định nghĩa
#  lưu data dưới dạng map giữa các key và Value

#khởi tạo sử dụng {}
name_age = {'jack': 90,'nam':20,'yuko':18} #{key:value}
print(len(name_age))
# để tạo dict rỗng
# name_age = dict()
# name_age = {}
#truy cập vào dict
print(f"age of jack : {name_age['jack']}")
print(f"age of yuko : {name_age['yuko']}")

#thêm vào dict, update giá trị
name_age['jack'] = 91
print(f"new age of jack : {name_age['jack']}")

#thêm
name_age['rin'] = 25
print(name_age)

# duyệt qua các phần tử của dict
#duyệt qua các key

for k in name_age:
    print(k)
# hoặc for k in name_age.keys():

#duyệt qua các value
for k in name_age.values():
    print(k)

#duyệt qua cả key và value sử dụng nhiều nhất
for k,v in name_age.items():
    print(f" name : {k} -- age : {v}")
