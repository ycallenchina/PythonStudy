
import re
line = "Cats are smarter than dogs";
# 正则基本方法:re.search
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

# 正则生成字典方法
q=re.search('(?P<province>\w{3})',line)
print(q.groupdict())
# 正则span用法:显示搜索得到的起始位,和末尾位
j=re.match(r'\w',line) 
print(j.span())
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  

# 正则返回搜索内容:group()和groups()用法
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("searchObj.groups圆括号里的字符 : ", searchObj.groups())
    
else:
    print("Nothing found")
