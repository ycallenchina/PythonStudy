# 输入 两个 文件名,复制第一个文件到第二个文件
# echo命令创建的文件用encoding='utf-16'解码
# 但是自建txt,不能用encoding='utf-16'解码.
from sys import argv

script,in_file,to_file=argv=argv

print(f'this is {script} file.\n now we are going to copy text.\n retrun to begin.')
input('>')

text=open(in_file,'r',encoding='utf-16')
data=text.read()
text2=open(to_file,'w')
text2.write(data)

print('now we are finish copy,retrun come over.')
input('>')
print('over')


