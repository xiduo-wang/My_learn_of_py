# 现实世界的事物大多可以归结为有两种特点：属性和行为
# 属性指的是事物自身的特点 行为指的是事物可以做出的动作
# 面向对象编程的特点：设计类、基于类创建对象、对象做具体的工作
# 演示：
# 创建一个闹钟类
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构建两个闹钟对象并让其工作
clock_1 = Clock()
clock_1.id = '00302'
clock_1.price = 19.9
print(f"闹钟id：{clock_1.id}，价格：{clock_1.price}")
clock_1.ring()
