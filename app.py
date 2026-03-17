import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- 1. 网页标题和侧边栏 ---
st.set_page_config(page_title="我的数学实验室", page_icon="🧮")

# 侧边栏 (Sidebar)
with st.sidebar:
    st.header("控制面板")
    user_name = st.text_input("请输入你的名字", "未来的数学家")
    st.info(f"你好，{user_name}！欢迎来到我的 Python 空间。")

    # 一个滑动条，控制下面图表的参数
    points = st.slider("选择数据点数量", 100, 2000, 500)

# --- 2. 主页面内容 ---
st.title("🌌 我的个人数学主页")
st.write("这是我从 IC 转行数学系的 **学习成果展示**。")
st.write("这也是我用 Python 搭建的第一个网页！")

st.divider()  # 分割线

# --- 3. 展示数学公式 ---
st.header("1. 数学之美")
st.markdown(r"""
既然是数学系，当然要展示最帅的公式：
$$
e^{i\pi} + 1 = 0
$$
或者这是著名的 **正态分布概率密度函数**：
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}
$$
""")

# --- 4. 交互式绘图 ---
st.header("2. 蒙特卡洛模拟演示")
st.write(f"正在模拟 {points} 个随机点...")

# 生成数据
data = pd.DataFrame(
    np.random.randn(points, 2),
    columns=['x', 'y']
)

# 直接用 Streamlit 自带的图表（基于 Altair，带交互功能）
st.scatter_chart(data)

# 或者用你熟悉的 Matplotlib
st.subheader("使用 Matplotlib 绘制正弦波")
fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)
ax.plot(x, y, color='purple')
ax.set_title("y = sin(x)")
st.pyplot(fig)  # 把图塞进网页

# --- 5. 互动小组件 ---
st.divider()
st.header("3. 留言板")
if st.button("点赞"):
    st.balloons()  # 屏幕会飘气球，超好玩！
    st.success("谢谢你的点赞！")

text = st.text_area("你想对我说什么？")
if text:
    st.write("收到留言：", text)