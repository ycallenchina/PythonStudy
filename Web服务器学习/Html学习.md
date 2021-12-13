### 复合选择器

#### 常用选择器

- | 选择器     | 写法           | 作用                              | 解释                       |
  | ---------- | -------------- | --------------------------------- | -------------------------- |
  | 后代选择器 | .nav a         | 用来选择后代的元素                | 选择类nav里的所有a标签     |
  | 子代选择器 | .nav>p         | 选择最近一级的元素,就是选择亲儿子 | 选择类nav下一级的所有p标签 |
  | 并集选择器 | .nav , .header | 选择相同样式的元素                | 选择统计下类nav和类header  |

#### 链接伪类选择器

- | 链接伪类选择器 | 选择                               |
  | -------------- | ---------------------------------- |
  | a:link         | 所有未被访问的链接                 |
  | a:visited      | 所有已被访问的链接                 |
  | a:hover        | 鼠标指针悬停的链接                 |
  | a:active       | 点击中的活动链接(鼠标按下未弹起来) |

- 伪类选择器的顺序:
  - link>visited>hover>active

#### :focus伪类光标选择器

- 用法:选择获得光标的元素

- 一般写法

  - ```
    input : focus {}
    ```



### CSS优先级

- | 选择器            | 选择器权重 |
  | ----------------- | ---------- |
  | 继承 或者 通配符* | 0,0,0,0    |
  | 元素选择器        | 0,0,0,1    |
  | 类选择器,伪类     | 0,0,1,0    |
  | ID选择器          | 0,1,0,0    |
  | 行内样式 style="" | 1,0,0,0    |
  | !important 重要的 | 最大       |

  

### 盒子模型

#### 一,总体介绍

- 盒子分位 content padding border margin 四大元素

  - content:为盒子内容
  - padding:为盒子的内边框:用于盒子内部排版
  - border:为盒子的边框线,用于设计盒子样式
  - margin:为盒子的外边框,用于隔开盒子与盒子的距离

  - 盒子示意图<img src="http://allenyc.cn/images/box.png" alt="盒子模型示意图" style="width:500px;" />

#### 二,边框border使用

- 写法

  - |     样式     | 写法                                   | 说明                           |
    | :----------: | -------------------------------------- | ------------------------------ |
    |     宽度     | width                                  |                                |
    |     高度     | heigh                                  |                                |
    |   线条样式   | border-style                           | 看下图                         |
    | 上下左右边框 | border-top,border-bottom,..left..right | 可以使用符合写法               |
    |   复合写法   | border: 1px soild pink;                | 3个基本属性:粗细,线条样式,颜色 |



- border线条样式表<img src="http://allenyc.cn/images/border_style.png" alt="盒子模型示意图" style="width:500px;" />

- boder 重合边框合并:用于表格边框中间过粗

  - ```
    border-collapse:collapse
    ```

    

#### 三,内边框padding使用

- 用法

  - | 写法                     | 意思                                 |
    | ------------------------ | ------------------------------------ |
    | padding:5px ;            | 表示上下左右都是5像素内边距          |
    | padding:5px 2px;         | 表示上下,左右是5,2像素内边距         |
    | padding:5px 2px 3px;     | 表示上,左右,下都是5,2,3像素内边距    |
    | padding:5px 2px 3px 4px; | 表示上,下,左,右都是5,2,3,4像素内边距 |

- 注意:padding 没有颜色属性

  


#### 四,外边框margin的使用

- 用法

  - ```
    margin:0 auto
    ```

    - 表示:上下外边框为0 左右外边框相同所以居中显示.




### Flex布局_弹性布局

#### 概述
- **描述**：Flex 是 Flexible Box 的缩写，意为"弹性布局"，用来为盒状模型提供最大的灵活性。任何一个容器都可以指定为 Flex 布局。

- **Flex 布局的结构**
	
	- flex container (flex容器/父项）
	- flex item （flex项目/父项的项目）
	
- **图示**
	
	- ![flex示意图](https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071004.png)
	
- 图示解释
	- flex container :flex 容器
	
	- main axis:主轴 (每个flex都默认横向从左到右为主轴)
	
	- cross axis: 侧轴 (自上往下为侧轴)
	
	- flex item ：flex 项目
	
	  

#### Flex 容器(父项)用法

- 定义此容器为flex 
	- ```
	   disply : flex ;
	  ```
- 定义flex主轴方向
	- ``` 
	      flex-direction:row; 横向从左到右
	      flex-direction:column;竖向从上往下
	      flex-direction:column reverse;竖向从下往上
	  ```
- 定义主轴上元素的排序方式
	- justify-content : flex-start(默认-从start到end）
		- flex-end 从end到start
		- center 居中
		- space-around 平分空间
		- space-between 头尾两侧 中间平分
	- 图示
		- ![主轴排序图示](https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png)
	
- 换行功能开启
	- ```
		flex-wrap:wrap (默认为nowrap)
- 侧轴上元素排列方式（单行情况nowrap）
	-  ```
		align-items: flex-start 从头到尾
		align-items: flex-end 从尾到头
		align-items: center 居中
		align-items: stretch 拉伸（没有高度才行）
		align-items: baseline: 项目的第一行文字的基线对齐。
	
	
- 示意图![侧轴排序](https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071011.png)

- 侧轴上元素排列方式（多行情况wrap)
	-  ```
		align-content: flex-start 从头到尾
		align-content: flex-end 从尾到头
		align-content: center 居中
		align-content: space-around 平分空间
		align-content: space-between 两侧打头中间平分

- 简写 主轴+换行格式 flex-flow
	- ```
		flex-flow: cloumn wrap (row nowrap 可选)
	  ```


#### Flex 子项(flex item)用法
- **子项权重 flex**
	- 子项权重默认是1
	- 若指定某个子项权重为2时
		``` flex:2; ```
	- 图示 ![子项权重](https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071014.png)
- **单独侧轴对齐**
	- 子项侧轴对齐默认为跟随父项
	- 若指定某个子项单独尾对齐时
		``` align-self:flex-end; ```
	- 图示 ![单独对齐](https://www.ruanyifeng.com/blogimg/asset/2015/bg2015071016.png)
- **单独排序**
	- 所有子项的默认排序order都为0
	- 若更改某个子项的order，小于0就会排到前面，大于0会排到后面
		``` order:-1; ```