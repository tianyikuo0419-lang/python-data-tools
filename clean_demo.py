
import pandas as pd

# 构造模拟数据，不涉及真实业务信息
df = pd.DataFrame({
    "学校": ["A大学", "B大学", "A大学"],
    "专业": ["计算机科学与技术", "统计学", "计算机科学与技术"]
})

# 去除重复记录
df_clean = df.drop_duplicates()

# 导出为 Excel 文件
df_clean.to_excel("demo_cleaned.xlsx", index=False)

print("数据清洗完成！")
    