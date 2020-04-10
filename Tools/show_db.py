def 数据动态对比图(数据源, 数据源_sheet='Sheet1'):
    '''# 输入:读取大于等于4列的excel表数据路径,取第2,3,4列分析,2为名字str,3为时间int,4为数值float
       # 输出:以3时间为变化参数,画2名字为纵,4为横坐标的动态图'''

    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import matplotlib.animation as animation
    from IPython.display import HTML
    # 可现实中文的设置
    plt.rcParams['font.sans-serif'] = ['fangsong']
    plt.rcParams['axes.unicode_minus'] = False

    df = pd.read_excel(数据源, 数据源_sheet)  # 读取excel,指数2017-2018数据
    df = df.iloc[:, 1:4]  # 获取2,3,4列所有行数据
    y_name=df.columns.values#获取df的列名

    # 封装
    def bar_chart_race(year):
        df_sort = df[df[y_name[1]] == year].sort_values(y_name[2])  # 按close列的倒叙排
        ax.clear()  # 清楚ax表内容
        # 重新画图
        ax.barh(df_sort[y_name[0]], df_sort[y_name[2]])  # 装载数据
        plt.title(f'{year}')  # 给标题为日期
        plt.box(False)  # 不明代码

    fig, ax = plt.subplots(figsize=(10, 18))  # 画图

    date_list = list(set(df[y_name[1]]))  # 去重复获取日期参数
    date_list.sort()  # 给日期从前往后排序
    #动态图函数
    animator = animation.FuncAnimation(fig, bar_chart_race, frames=date_list)  # fig图,bar主参,frames是日期变化参数.
    HTML(animator.to_jshtml())  # 不明代码

    plt.show()