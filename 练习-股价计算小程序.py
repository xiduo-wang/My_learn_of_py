name = "传智播客"
stock_code = "003032"
stock_price = 19.99
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}",f"股票代码：{stock_code}",f"当前股价：{stock_price}")
print("每日的增长系数为：%2.1f" %stock_price_daily_growth_factor,"经过了%d" %growth_days,"天的增长","股价达到了：%.2f" %(stock_price * stock_price_daily_growth_factor ** growth_days))
"""
该程序计算了股价在七天后的价格 
其中第一行输出使用了快捷格式化
第二行使用传统方法并满足了练习要求的数字宽度及小数点精度
"""