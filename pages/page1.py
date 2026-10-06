import streamlit as st

st.set_page_config(
    page_title="Iris Flowers",
    page_icon="🌸",
    layout="wide"
)

st.title("🌸 Iris Flowers")

st.write("""
The Iris dataset is one of the most commonly used datasets
for learning machine learning and data analysis.
""")

st.subheader("The Three Iris Species")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
        caption="Iris Versicolor",
        use_container_width=True
    )
    st.write("**Iris Versicolor**")

with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
        caption="Iris Virginica",
        use_container_width=True
    )
    st.write("**Iris Virginica**")

with col3:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
        caption="Iris Setosa",
        use_container_width=True
    )
    st.write("**Iris Setosa**")

st.markdown("---")

st.subheader("About the Dataset")

st.write("""
The dataset contains measurements of iris flowers.

The four main features are:

- 🌱 Sepal Length
- 🌱 Sepal Width
- 🌸 Petal Length
- 🌸 Petal Width

The target variable is the Iris species.
""")