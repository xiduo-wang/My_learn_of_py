import numpy as np
import matplotlib.pyplot as plt

# ================= 全局参数 =================
# 池体参数
L, W, H = 2.0, 1.5, 0.5  # 池体尺寸(m)
A_bottom = L * W  # 池底面积(m²)
A_walls = 2 * (L + W) * H  # 侧壁面积(m²)
A_surface = L * W  # 水面面积(m²)
ρ = 1000  # 水密度(kg/m³)
c_p = 4718  # 比热容(J/(kg·K))

# 热力学参数
U_bottom = 1.934  # 池底热损系数(W/(m²·K))
U_walls = 3.804  # 侧壁热损系数(W/(m²·K))
U_surface = 4.692  # 水面热损系数(W/(m²·K))
T_env = 10  # 环境温度(℃)
T_hot = 50  # 注水温度(℃)
Q_heater = 10e3 * A_bottom  # 池底加热功率(W)

# 经济参数
electricity_price = 0.8  # 电费(元/度)
water_price = 5  # 水费(元/吨)


# ================= 模型检验 =================
def energy_balance_validation(m_dot):
    """能量守恒验证"""
    # 稳态条件假设
    T_steady = 45  # 目标温度(℃)

    # 输入能量
    Q_injection = m_dot * c_p * (T_hot - T_steady)
    Q_heating = Q_heater

    # 热损失
    Q_loss = (U_bottom * A_bottom + U_walls * A_walls + U_surface * A_surface) * (T_steady - T_env)

    # 守恒误差
    error = abs(Q_injection + Q_heating - Q_loss) / (Q_injection + Q_heating) * 100
    print(f"能量守恒误差：{error:.2f}% (ṁ={m_dot}kg/s)")
    return error


def numerical_stability_test():
    """数值稳定性分析"""
    dt_list = [10, 30, 60, 120]
    m_dot = 1.2
    final_temps = []

    for dt in dt_list:
        steps = 1800 // dt
        T = 30
        for _ in range(steps):
            Q_in = m_dot * c_p * (T_hot - T)
            Q_loss = (U_bottom * A_bottom + U_walls * A_walls + U_surface * A_surface) * (T - T_env)
            dT = (Q_in + Q_heater - Q_loss) * dt / (ρ * L * W * H * c_p)
            T += dT
        final_temps.append(T)

    plt.figure(figsize=(8, 4))
    plt.plot(dt_list, final_temps, 'bo-')
    plt.axhline(45, color='r', linestyle='--')
    plt.xlabel('时间步长(s)')
    plt.ylabel('最终温度(℃)')
    plt.title('数值稳定性分析（ṁ=1.2kg/s）')
    plt.grid(alpha=0.3)
    plt.show()


# ================= 灵敏度测试 =================
def parameter_sensitivity(base_m=1.2):
    """关键参数灵敏度分析"""
    T_steady = 45  # 明确定义目标温度

    params = {
        '环境温度': (T_env, [+5, -5]),
        '热损失系数': (1.0, [+0.2, -0.2]),  # 比例系数
        '注水温度': (T_hot, [+2, -2]),
        '加热功率': (10e3, [+5e3, -5e3])  # W/m²
    }

    results = {}
    for param, (base_val, variations) in params.items():
        delta_m = []
        for delta in variations:
            # 临时修改参数
            if param == '环境温度':
                T_env_temp = base_val + delta
                Q_loss_factor = (T_steady - T_env_temp) / (T_steady - T_env)
            elif param == '热损失系数':
                Q_loss_factor = 1 + delta
            elif param == '注水温度':
                T_hot_temp = base_val + delta
                Q_in_factor = (T_hot_temp - T_steady) / (T_hot - T_steady)
            elif param == '加热功率':
                Q_heater_temp = (base_val + delta) * A_bottom

            # 计算新ṁ
            if param in ['环境温度', '热损失系数']:
                new_m = base_m * Q_loss_factor
            elif param == '注水温度':
                new_m = base_m / Q_in_factor
            elif param == '加热功率':
                new_m = base_m - (delta / 5e3) * 0.3  # 经验公式

            delta_m.append(abs(new_m - base_m))

        results[param] = delta_m

    # 可视化
    labels = list(results.keys())
    positive = [val[0] for val in results.values()]
    negative = [val[1] for val in results.values()]

    x = np.arange(len(labels))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x - width / 2, positive, width, label='正向扰动')
    plt.bar(x + width / 2, negative, width, label='负向扰动')

    plt.xticks(x, labels)
    plt.ylabel('注水速率变化量(kg/s)')
    plt.title('关键参数灵敏度分析')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.show()


# ================= 执行检验与测试 =================
if __name__ == "__main__":
    print("===== 模型检验 =====")
    energy_balance_validation(1.2)
    numerical_stability_test()

    print("\n===== 灵敏度测试 =====")
    parameter_sensitivity()