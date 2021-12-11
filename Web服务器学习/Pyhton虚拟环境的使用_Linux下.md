# Pyhton虚拟环境的使用_Linux下

### 一,安装虚拟机

```
sudo pip3 install virtualenv
```

​		此代码选择pip3 是为了避免在python2中安装了.



### 二,创建虚拟机环境

- #### 创建虚拟环境存放文件夹
  - ```
    mkdir 文件名A
    cd 文件夹A
    ```

- #### 在文件夹下创建虚拟环境

  - ```
    virtualenv -p python3 venv
    ```



### 三,激活虚拟环境

```
source venv/bin/activate
```

​	效果:命令行前面显示 (venv)

​	`注意:此条命令 应该在刚才创建的 文件夹A 目录下执行,因为activate开启命令存放路径是: 文件夹A/venv/bin/activte` 



### 四,退出虚拟环境

```
deativate
```

