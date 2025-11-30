# 继承的通俗含义就是在一个老的类上进行添加、删除或修改从而创建一个新的类
# 单继承
"""
class 类名(父类名)
     类内容体
"""
class Phone:
    IMEI = None
    producer = 'xiduo'

    def call_by_4g(self):
        print("这是4g通话")

class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = Phone2022()
print(phone.producer)  # 父类变量
phone.call_by_5g()   # 子类方法

# 多继承 ：继承多个父类 按从左到右顺序继承
"""
class 类名(父类1,父类2,.......)
    类内容体
"""
class NFC_reader:
    nfc_type = "第五代"
    producer = 'xiduo'

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = '红外遥控'

    def control(self):
        print("红外遥控开始了")

class MyPhone(Phone,NFC_reader,RemoteControl):
    pass  # pass关键字(不想在新的类中添加变量和方法时使用)

phone2 = MyPhone()
phone2.read_card()
phone2.control()

# 多继承下 父类成员变量名一致的解决办法
# 在上述情况下 在调用时遵循先到先得的原则(显示先定义的)