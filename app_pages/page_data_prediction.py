import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

def prediction_page():
    st.title('Data Prediction')
    st.write("Upload an image of a cherry leaf to determine if it is healthy or has powdery mildew.")

    model = load_model('outputs/v1/cherry_leaves_modelv1.keras')

    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = image.load_img(uploaded_file, target_size=(224, 224), color_mode='rgb')
        st.image(img, caption='Uploaded Image', use_column_width=True)
        
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match expected input shape
        img_array = img_array.astype('float32') / 255.0  # Normalize the image
        
        pred_proba = model.predict(img_array)[0][0]
        
        target_map = {0: 'Healthy', 1: 'Powdery Mildew'}
        pred_class = target_map[int(pred_proba > 0.5)]

        st.write(f"Prediction Probability: {pred_proba:.2f}")
        st.write(f"Predicted Class: {pred_class}")

prediction_page()

