import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 라이브러리 import (사용자가 설치한 후 사용)
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Matplotlib 예시
st.header("Matplotlib 예시")
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.figure(figsize=(8, 4))
plt.plot(x, y, marker='o')
plt.title("간단한 선 그래프")
plt.xlabel("X 축")
plt.ylabel("Y 축")
st.pyplot(plt)
plt.clf()  # 그래프 클리어

# Seaborn 예시
st.header("Seaborn 예시")
data = np.random.randn(100, 2)
plt.figure(figsize=(8, 4))
sns.scatterplot(x=data[:, 0], y=data[:, 1])
plt.title("Seaborn 산점도")
st.pyplot(plt)
plt.clf()

# Plotly 예시
st.header("Plotly 예시")
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Iris 데이터셋 산점도")
st.plotly_chart(fig)
