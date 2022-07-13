
#!/usr/bin/python

from os.path import basename, isdir, isfile
from os import listdir


def traverse(path, depth=0):
    prefix = depth * '| ' + '|_'

    # 判断是否文件夹
    if(isdir(path)) and ('.git' not in path):
        # 重新遍历此文件夹,读出文件数量(不包括文件夹)
        k = 0
        for item in listdir(path):
            item_path = path+"/"+item
            if(isfile(item_path)):
                k += 1

        print(prefix, basename(path), k)

        for item in listdir(path):
            traverse(path+'/'+item, depth+1)
    else:
        pass
        # print (prefix, basename(path))


if __name__ == '__main__':
    traverse('C:/Users/YcAllenEffy/Desktop/PythonStudy_Git')
 