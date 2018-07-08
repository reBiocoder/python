import  re
str="ahsuahfasf2018-06-28dfafdasg"
s=re.findall(r'(\d{4}-\d{2}-\d\d)',str)
print(s[0])