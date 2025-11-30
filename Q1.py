# -*- coding: utf-8 -*-
import numpy as np
from scipy.io import loadmat


# --------------------------
# 1. 加载.mat文件（增加dtype处理）
# --------------------------
def load_mat_data(file_path):
    """加载MATLAB数据文件并转换数据类型"""
    data = loadmat(file_path)
    # 强制转换为int64防止溢出
    data['a'] = data['a'].astype(np.int64)
    data['b'] = data['b'].astype(np.int64)
    data['c'] = data['c'].astype(np.int64)
    return data


mat_data = load_mat_data('校赛题1附录数据.mat')

# 提取关键矩阵
a = mat_data['a']  # 元件价格矩阵
b = mat_data['b']  # 组装费用矩阵
c = mat_data['c']  # 销售价格矩阵


# --------------------------
# 2. 数据预处理（增加空列表保护）
# --------------------------
def get_valid_types(price_matrix):
    """获取有效型号列表并校验数据范围"""
    valid = {}
    for i in range(3):
        valid_indices = np.where(price_matrix[i, :] > 0)[0]
        # 增加数值范围校验
        if np.any(price_matrix[i, valid_indices] > np.iinfo(np.int64).max // 3):
            raise ValueError("元件价格超出int64处理范围")
        valid[f'元件{i + 1}'] = (valid_indices + 1).tolist()  # MATLAB索引
    return valid


valid_types = get_valid_types(a)

# --------------------------
# 3. 枚举计算（记录详细成本信息）
# --------------------------
max_profit = -np.inf
best_details = {
    "combination": (0, 0, 0),
    "costs": (0, 0, 0),
    "assembly": 0,
    "sale": 0
}

# 优化遍历顺序（按成本升序排列加快剪枝）
valid_types['元件1'].sort(key=lambda x: a[0, x - 1])
valid_types['元件2'].sort(key=lambda x: a[1, x - 1])
valid_types['元件3'].sort(key=lambda x: a[2, x - 1])

for x1 in valid_types['元件1']:
    cost_x1 = a[0, x1 - 1]
    # 提前剪枝：如果单个元件成本已超过历史最高售价则跳过
    if cost_x1 > c.max():
        continue

    for x2 in valid_types['元件2']:
        cost_x2 = a[1, x2 - 1]
        if (cost_x1 + cost_x2) > c.max():
            continue

        for x3 in valid_types['元件3']:
            cost_x3 = a[2, x3 - 1]
            total_cost = cost_x1 + cost_x2 + cost_x3

            # 三维索引安全校验
            try:
                assembly_cost = b[x1 - 1, x2 - 1, x3 - 1]
                sale_price = c[x1 - 1, x2 - 1, x3 - 1]
            except IndexError:
                print(f"索引越界: ({x1}, {x2}, {x3})")
                continue

            profit = sale_price - total_cost - assembly_cost

            if profit > max_profit:
                max_profit = profit
                best_details = {
                    "combination": (x1, x2, x3),
                    "costs": (cost_x1, cost_x2, cost_x3),
                    "assembly": assembly_cost,
                    "sale": sale_price
                }

# --------------------------
# 4. 增强型输出
# --------------------------
print("\n========== 最优决策方案 ==========")
print(f"元件组合：")
print(f"  元件1-型号{best_details['combination'][0]}（价格：{best_details['costs'][0]}元）")
print(f"  元件2-型号{best_details['combination'][1]}（价格：{best_details['costs'][1]}元）")
print(f"  元件3-型号{best_details['combination'][2]}（价格：{best_details['costs'][2]}元）")
print(f"组装费用：{best_details['assembly']}元")
print(f"市场售价：{best_details['sale']}元")
print("---------------------------------")
print(f"总成本：{sum(best_details['costs']) + best_details['assembly']}元")
print(f"最大利润={best_details['sale']}元-{sum(best_details['costs']) + best_details['assembly']}元-{best_details['assembly']}元={max_profit}元")
