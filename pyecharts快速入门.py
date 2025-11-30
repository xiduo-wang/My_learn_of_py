# 构建一个基础的折线图
# 使用全局变量项设置属性
# 导入line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 得到折线图对象
line = Line()
# 添加x轴数据 add_xaxis方法
line.add_xaxis(['中国','美国','英国'])
# 添加y轴数据 add_yaxis方法
line.add_yaxis('GDP',[30,20,10])
# 生成图表 render方法帮助将代码转换为图表
# line.render()
# 在文件夹中可以找到html类型文件 用浏览器打开即可预览
# 全局配置与系列配置
# 全局配置针对整个图像进行设置 系列配置针对具体的轴数据进行设置
# set_global_opts方法
# 其中有几个选项
"""
TirleOpts:标题配置项
LengendOpts:图例配置项
ToolboxOpts:工具箱配置项
VisualMapOpts:视觉映射配置项
"""
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),   # 第一个参数控制名称,第二个参数控制左右位置 第三个参数控制上下位置
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
# 此处只展示几种常见全局配置项 想了解更多可以查看pyecharts官方网站
line.render()