# 掌握复写父类成员语法 掌握在子类中调用父类成员
# 复写
# 子类继承父类的成员属性和成员方法后，如果想修改父类中的属性或方法 可使用复写
# 即在子类中重新定义同名属性/方法
# 演示：
class Phone:
    IMEI = None
    producer = 'xiduo'

    def call_by_5g(self):
        print("使用5g网络进行通话")
# 进行复写
class MyPhone(Phone):
    producer = 'lbh' # 复写步骤

    def call_by_5g(self):
        print("开启CPU单核模式")
        print(f"父类的厂商是:{super().producer}")
        Phone.call_by_5g(self)
phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

# 调用父类同名成员
# 如果需要使用被复写的父类成员，需要使用特殊的调用方式
"""
语法1：父类名.成员变量
      父类名.成员方法(self)
语法2：
      super().成员变量
      super().成员方法()
"""