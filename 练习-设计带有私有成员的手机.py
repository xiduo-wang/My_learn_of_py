class Phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:    # 变量本身赋值为布尔类型，不需要再做判断
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
phone = Phone()
phone.call_by_5g()