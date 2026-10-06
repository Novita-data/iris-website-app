import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris


st.set_page_config(
    page_title="Data Exploration",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Iris Dataset - Data Exploration")


# Load Iris dataset
iris = load_iris()


# Convert dataset into DataFrame
df = pd.DataFrame(
    iris.data,
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)


# Add species names
df["species"] = [
    iris.target_names[i]
    for i in iris.target
]


# Dataset Preview
st.subheader("Dataset Preview")

st.dataframe(df)


st.markdown("---")


# Dataset Information
st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Number of Rows", df.shape[0])

with col2:
    st.metric("Number of Columns", df.shape[1])

with col3:
    st.metric(
        "Missing Values",
        df.isnull().sum().sum()
    )


st.markdown("---")


# Statistical Summary
st.subheader("Statistical Summary")

st.dataframe(df.describe())


st.markdown("---")


# Species Distribution
st.subheader("Species Distribution")

fig, ax = plt.subplots()

sns.countplot(
    data=df,
    x="species",
    ax=ax
)

ax.set_xlabel("Species")
ax.set_ylabel("Count")

st.pyplot(fig)


st.markdown("---")


# Feature Analysis
st.subheader("Feature Analysis")

feature = st.selectbox(
    "Select a feature",
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)


fig, ax = plt.subplots()

sns.boxplot(
    data=df,
    x="species",
    y=feature,
    ax=ax
)

ax.set_xlabel("Species")
ax.set_ylabel(feature)

st.pyplot(fig)