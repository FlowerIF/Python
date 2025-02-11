# loop in py
my_list = [1,2,3,4,5]

#for
for i in my_list:
    print(i)
for i in range(len(my_list)):
    print(i)

# while
count = 2
while count < 5:
    print("hi ae")
    count = count + 1
# break và continue
# for i in my_list:
#     print(i)
#     if i == 3:
#         break
    


for i in my_list:
    if i == 3:
        continue
    print(i)