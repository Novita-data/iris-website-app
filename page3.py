import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Iris Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Iris Flower Prediction")

st.write(
    "Enter the measurements of an Iris flower "
    "to predict its species."
)

st.markdown("---")

st.subheader("Enter Flower Features")

col1, col2 = st.columns(2)

with col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with col2:

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

st.markdown("---")

if st.button("🔮 Predict Species"):

    # Arrange input values
    input_data = np.array([
        [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]
    ])

    # Load model
    with open("iris_model", "rb") as file:
        model = pickle.load(file)

    # Prediction
    prediction = model.predict(input_data)

    st.success(
        f"🌸 Predicted Species: **{prediction[0]}**"
    )