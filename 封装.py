# 理解封装的概念
# 掌握私有成员的使用
# 面向对象编程：基于模板(类)去创建实体(对象),使用对象来完成功能开发
# 面向对象主要包含三大特征：封装、继承、多态
# 封装表示的是将现实世界中事物的属性、行为，封装到类中，描述为：成员变量、成员方法
# 类中提供了同现实事物相同的不公开的属性和方法的私有成员
# 私有成员变量：变量(方法)名以__开头即可
# 演示
class Phone:

    __current_voltage = 1

    def __keep_single_core(self):
        print("让cpu以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，已转换为单核模式运行")
phone = Phone()
# 该条命令无法执行(私有成员方法)
# phone.__keep_single_core()
# (私有成员变量)
# print(__current__voltage)

# 私有成员无法被直接使用 但可以被其它的成员直接使用
phone.call_by_5g()

# 私有成员的意义：在类中提供仅供内部使用的属性和方法