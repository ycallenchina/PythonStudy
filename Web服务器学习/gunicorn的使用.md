# gunicorn的使用

### 一,安装

- ```
  pip install gunicorn
  ```

  - 提示:在虚拟环境中安装.



### 二,激活(手动)

- ```
  gunicorn -w 3 -b 0.0.0.0:9001 run:app
  ```

  - -w :表示进程数量上限设置 此时为3
  - -b :表示占用ip端口
  - run:表示在此路径下 运行程序名字(不需要后缀)
  - app:表示程序里运行的方法名



### 三,加载gunicorn配置文件激活

- ```
  gunicorn -c 配置文件路径 run:app
  ```

  - 配置文件使用见<Web开发_明日科技>p73页.



### 四,在supervisor中启动

- 配置文件修改如下
  - ```
    command=/www/flask_test/venv/bin/gunicorn -c gunicorn/gunicorn_conf.py test:app
    directory=/www/flask_test
    ```

    - /www/flask_test/venv/bin/gunicorn :为gunicorn 启动路径 
    - gunicorn/gunicorn_conf.py :为配置文件路径
    - test:为在directory下运行的程序民
    - app:为程序里的方法