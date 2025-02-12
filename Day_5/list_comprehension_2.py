#best practice

# multiple loops

# list lồng nhau
nested_lst = [[i for i in range(5)] for _ in range(5)]
print(nested_lst)

arr_2d = [
    [1,2,3],
    [3,4,5],
    [9,9,10]
]
# sử dụng forr
# new_l = []
# for r in arr_2d:
#     for num in r:
#         new_l.append(num)
# print(new_l)

# sử dụng list comprehension
flatten_lst = [num for row in arr_2d for num in row]
print(flatten_lst)