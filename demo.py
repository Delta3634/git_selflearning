##自学
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel(r"quartile_test_data.xlsx")

# 初始化一个字典，用于存储每列的异常值
outliers_dict = {}

# 遍历每一列数据
for column in df.columns:
    # 获取列数据
    values = df[column]

    # 计算Q1（第25百分位数）和Q3（第75百分位数）
    Q1 = values.quantile(0.25)
    Q3 = values.quantile(0.75)

    # 计算四分位距（IQR）
    IQR = Q3 - Q1

    # 计算上下限
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # 识别异常值
    outliers = values[(values < lower_bound) | (values > upper_bound)]
    outliers_dict[column] = outliers

    # 绘制箱型图
    plt.figure(figsize=(10, 6))
    plt.boxplot(values, vert=False)
    plt.title(f'Boxplot of {column} with Outliers')
    plt.xlabel(column)

    # 显示箱型图
    plt.show()

# 输出各列的异常值
for column, outliers in outliers_dict.items():
    print(f"列 {column} 的异常值：")
    print(outliers)