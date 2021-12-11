# BootStrap使用

### 一,安装

1. [官网下载用于生产环境的booststrap](https://v3.bootcss.com/)

2. 解压压缩包存放至index.html目录下

3. 在index.html 下,插入IE9兼容代码,以及引用样式代码

   - ```html
         <!--[if lt IE 9]>
           <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
           <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
         <![endif]-->
     ```

   - ```html
     <!-- 引入bootstrap 样式文件 -->
     <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
     <!-- 引入我们自己的首页样式文件 ,自己样式文件存放在css下index.css里-->
     <link rel="stylesheet" href="css/index.css">
     ```

4. 书写

   - 此处省略,遵循bosststrap 样式规则.详情看官网介绍.



### 二,BootStrap响应式布局介绍

#### 1.布局容器

- `.container` 类用于固定宽度并支持响应式布局的容器。

  - ```
    <div class="container">
      ...
    </div>
    ```

    

- `.container-fluid` 类用于 100% 宽度，占据全部视口（viewport）的容器。

  - ```
    <div class="container-fluid">  
    ...
    </div>
    ```

    

#### 2. 12列栅格化系统,实现响应式布局

- 每个类对应不同宽度分辨率下的使用说明:

  - |                       | 超小屏幕 手机 (<768px)     | 小屏幕 平板 (≥768px)                               | 中等屏幕 桌面显示器 (≥992px)                       | 大屏幕 大桌面显示器 (≥1200px)                      |
    | :-------------------- | :------------------------- | :------------------------------------------------- | :------------------------------------------------- | -------------------------------------------------- |
    | 类前缀                | `.col-xs-`                 | `.col-sm-`                                         | `.col-md-`                                         | `.col-lg-`                                         |
    | 栅格系统行为          | 总是水平排列               | 开始是堆叠在一起的，当大于这些阈值时将变为水平排列 | 开始是堆叠在一起的，当大于这些阈值时将变为水平排列 | 开始是堆叠在一起的，当大于这些阈值时将变为水平排列 |
    | `.container` 最大宽度 | None （自动）              | 750px                                              | 970px                                              | 1170px                                             |
    | 列（column）数        | 12                         | 12                                                 | 12                                                 | 12                                                 |
    | 最大列（column）宽    | 自动                       | ~62px                                              | ~81px                                              | ~97px                                              |
    | 槽（gutter）宽        | 30px （每列左右均有 15px） |                                                    |                                                    |                                                    |

    - col-xs :表示在屏幕`<768px`像素时候,总是`横向`水平排列.
    - col-sm :表示在屏幕`≥768px`像素时候,采用栅格化`横向`排列,不然就标准流竖向排列.

    - cos-md :表示在屏幕`≥992px`像素时候,采用栅格化`横向`排列,不然就标准流竖向排列.

    - col-lg :表示在屏幕`≥1200px`像素时候,采用栅格化`横向`排列,不然就标准流竖向排列.

#### 3. 在不同分辨率下 隐藏/显示内容

- 响应式工具

  - | 显示状态 | 超小屏幕手机 (<768px) | 小屏幕平板 (≥768px) | 中等屏幕桌面 (≥992px) | 大屏幕桌面 (≥1200px) |
    | :------- | :-------------------- | :------------------ | :-------------------- | -------------------- |
    | 仅可见   | `.visible-xs-*`       | `.visible-sm-*`     | `.visible-md-*`       | `.visible-lg-*`      |
    | 隐藏     | `.hidden-xs`          | `.hidden-sm`        | `.hidden-md`          | `.hidden-lg`         |



#### 4. 配合css 媒体查询

- ```
  @media screen and (max-width:767px)
  	.nav li{
          float: left;
          width: 20%
      }
  ```

  - 意思:在屏幕 最大宽度767像素内:类nav d的所有li 改为向左流体布局,每个宽度为20%.

#### 5. 其他功能,查阅bootstrap官网文件

- 栅格嵌套:栅格下嵌套后栅格还是12个

- 列偏移:使用 `.col-md-offset-*` 类可以将列向右侧偏移 *表示偏移的栅格列数

- 列排序:通过使用 `.col-md-push-*` 和 `.col-md-pull-*` 类就可以改变列（column）的横向顺序, push:向右推,pull:向左拉.
