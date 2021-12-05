from pyecharts import options as opts
from pyecharts.charts import Liquid

def echarts_lq():
    c = (
    Liquid()
    .add("lq", [0.2, 0.8]) #第一个参数为显示字样参数，第二个参数为水位参数 
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-示例"))
    )
    c.render()

def echarts_line():

    # 导入配置项
    from pyecharts import options as opts
    # ChartType：图标类型，SymbolType：标记点类型
    from pyecharts import options as opts
    from pyecharts import options as opts
    from pyecharts.charts import Sankey
    from pyecharts .globals import ChartType, SymbolType
    from pyecharts.charts import Bar,Line,Grid

    A = ["小米","三星","华为","苹果","魅族","VIVO","OPPO"]
    CA = [100,125,87,90,78,98,118]
    B = ["草莓","芒果","葡萄","雪梨","西瓜","柠檬","车厘子"]
    CB = [78,95,120,102,88,108,98]



    line = Line()
    line.add_xaxis(B)
    line.add_yaxis("商家A",CA)
    line.add_yaxis("商家B",CB)
    line.set_global_opts(title_opts=opts.TitleOpts(title="2图",pos_top="10%"),#标题位置
                        legend_opts=opts.LegendOpts(pos_top="10%"))#选择标签的位置
    # line.render()

    bar = Bar()
    bar.add_xaxis(B)
    bar.add_yaxis("商家A",CA)
    bar.add_yaxis("商家B",CB)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="多图绘制"))

    bar.overlap(line)#在bar里放入line多图

    bar.render()


    #上下放两图
    # grid = Grid()
    # grid.add(bar,grid_opts=opts.GridOpts(pos_bottom="50%"))
    # grid.add(line,grid_opts=opts.GridOpts(pos_top="50%"))
    # grid.render()

if __name__ == '__main__':
    echarts_line()