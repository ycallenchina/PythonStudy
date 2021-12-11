# Supervisor使用：

[TOC]

### 一，安装

```shell
pip istall supervisor
```

### 二，查看配置文件

```
echo_supervisord_conf
```

​		**此时**，显示配置文件内容，其中以 ；开头都是注释说明内容

### 三，拷贝配置文件到当前并修改

```
echo_supervisord_conf > superviosrd_conf
```

​		此时,supervisord_conf文件为配置文件，打开后可在最后一行追加：

```
[include]
files = etc/webapp/*.ini
```

​		追加的类容意思:在etc/webapp文件里所有后缀.ini的文件随supervisor自动启动。

​		`提示:修改配置文件语法,每条语句前面带;号的,表示已经注释了不会被执行.`

> 注意:在默认tmp的文件目录下会被linux删除,加载配置文件时会报错:
>
> unix:///tmp/supervisor.scok不存在,解决方法时把tmp换成var/run 和var/log,具体内容见<Web开发一书>79页.


### 四，加载改好的配置文件，启动supervisor

```
supervisord -c www/supervisord_conf
```

​		-c 为加载的意思 www/supervisord_conf 表示刚才改好的配置文件在www文件夹里。

​		第二次启动不需要重复加载就只需要 supervisord 即可

```
supervisord
```

### 五，在指定etc/webapp/ 自动启动的路径下 创建需要加载的项目

```
vim 项目名.ini
```

​		项目创建规则在PythonStudy里面Web服务器学习目录下。

### 六，重新加载supervisor

```
supervisorctl reload
```

​	此时 项目名.ini会自动启动。

### 七，查看supervisor 运行的项目

```
supervisorctl status
```

### 八，退出，和启动某个项目

```
supervisorctl start 项目
supervisorctl stop 项目
```

### 九，退出supervisor

```
supervisorctl shutdown
```

### 十，总结 supervisor 语法

```
supervisord 用来启动suervisor
supervisorctl 启动supervisor后用来控制运行supervisor
```
