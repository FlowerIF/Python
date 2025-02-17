# có sẵn module re
import re
my_str = "xin chao tat ca moi nguoi, tat ca chung ta, moi nguoi co nghe ro khong"
# re.match() tìm kiếm ở đầu, thấy sẽ trả về, không khớp ở đầu xẽ trả về none

match = re.match('xin chao',my_str)
print(match)  # trả về <re.Match object; span=(0, 8), match='xin chao'>
print(match.span()) # trả về (0, 8)
print(match.group()) # trả về xin chao

# re.search() tìm kiếm các obj khớp ở bất kì đoạn nào, chỉ trả về vị trí khớp đầu tiên
match_re = re.search("tat ca",my_str)
print(match_re)  
print(match_re.span()) 
print(match_re.group()) 

# re.findall() trả về list tất cả các obj khớp
match_fi = re.findall("moi nguoi",my_str)
print(match_fi) # trả về list ['moi nguoi', 'moi nguoi']
print(type(match_fi))

# re.split() chia đoạn text dựa trên một số ký tự , có thêm ,maxsplit để thể hiện số lần chia tách đoạn
match_spl = re.split("tat",my_str, maxsplit=1)
print(match_spl)


# re.sub() thay thế 1 hoặc nhiều obj khớp bằng text khác
match_sub = re.sub("xin chao","hello",my_str)
print(match_sub)