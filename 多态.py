# 理解多态的概念
# 理解抽象类(接口)的概念及编程思想
# 多态的概念
# 指的是多种状态 即完成某个行为时 使用不同的对象会得到不同的状态
# 即同样的行为 传入不同的对象 得到不同的结果
class Animal:
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print("狗在吃骨头")

class Cat(Animal):
    def eat(self):
        print("猫在吃鱼")

def eat(animal: Animal):
    animal.eat()
dog = Dog()
cat = Cat()
eat(dog) # 狗在吃骨头
eat(cat) # 猫在吃鱼

# 演示抽象类(接口)的概念及编程思想
# 抽象类(接口)是一种抽象概念 它定义了类的行为 但不提供具体实现
# 抽象类不能实例化 但可以被继承
# 抽象类可以定义方法 但不能定义属性
# 抽象类可以被子类继承 子类可以实现抽象类中定义的方法
# 上面的Animal类就是一个抽象类
# 我们可以定义一个Animal的子类 如Dog类 它实现了Animal类的eat方法
# 这样我们就可以通过Dog类来调用eat方法 而不需要知道具体的实现
# 这样的编程思想就是面向接口编程
class AC:     # 抽象类
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass
class Mide(AC):    # 子类
    def cool_wind(self):
        print("Mide在吹冷风")
    def hot_wind(self):
        print("Mide在吹热风")
    def swing_l_r(self):
        print("Mide在左右摆动")

mide = Mide()
mide.cool_wind() # Mide在吹冷风
mide.hot_wind() # Mide在吹热风
mide.swing_l_r() # Mide在左右摆动