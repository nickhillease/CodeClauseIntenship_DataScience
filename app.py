import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
import joblib
from tensorflow.keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt
predictions=["Mild","Moderate","NO_DR","Proliferate_DR","Severe"]
# Title and description
st.title('Diabetic Retinopathy Detection')
st.write('Upload an image for prediction.')

# File upload
uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    RGBImg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    RGBImg = cv2.resize(RGBImg, (224, 224))
    image = np.array(RGBImg) / 255.0
    image = preprocess_input(image)

    # Load your model
    model = joblib.load('diabretino.pkl')  # Replace with the path to your trained model

    # Make predictions
    predict = model.predict(np.array([image]))
    pred = np.argmax(predict, axis=1)

    # Display the prediction
    st.write(f"Predicted Class: {predictions[pred[0]]}")


     