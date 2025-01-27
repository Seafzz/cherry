import streamlit as st

def page_summary_body():
    st.title('Summary')

    st.header("Project Background")
    st.write("""
    **Marianne McGuineys**, the head of IT and Innovation at Farmy & Foods, is facing a significant challenge with their cherry plantations. The presence of powdery mildew, a fungal disease affecting a wide range of plants, threatens their finest product in the portfolio. Currently, the manual inspection process is not scalable, taking 30 minutes per tree for inspection and 1 minute to apply a compound if needed. With thousands of cherry trees across multiple farms, this manual process is highly inefficient.
    """)

    st.header("Objective")
    st.write("""
    To address this challenge, Farmy & Foods' IT team proposed developing a machine learning (ML) system capable of instantly detecting powdery mildew in cherry leaves using images. The goal is to replace the time-consuming manual inspection process with an automated, scalable solution. Successful implementation could also be extended to other crops.
    """)

    st.header("Business Requirements")
    st.write("""
    - Conduct a study to visually differentiate between healthy cherry leaves and those affected by powdery mildew.
    - Develop a predictive model to determine if a cherry leaf is healthy or infected with powdery mildew.
    - Deliver a user-friendly dashboard that allows for easy interaction and visualization of the results.
    """)

    st.header("Methods")
    st.write("""
    - **Data Collection**: Gather images of healthy and infected cherry leaves from Farmy & Foods' dataset.
    - **Data Preprocessing**: Augment and rescale the images to enhance the model's performance.
    - **Model Development**: Build a convolutional neural network (CNN) for image classification.
    - **Training**: Train the model using the augmented image data and implement early stopping to optimize training efficiency.
    - **Evaluation**: Assess the model's accuracy and performance on validation and test datasets.
    """)

    st.header("Expected Outcomes")
    st.write("""
    - A highly accurate model for detecting powdery mildew in cherry leaves.
    - Visualizations comparing healthy and infected leaves.
    - An interactive dashboard for users to upload and classify their own leaf images.
    """)

    st.header("Conclusion")
    st.write("""
    This project aims to leverage machine learning to provide a scalable solution for detecting powdery mildew in cherry plantations, ultimately contributing to more efficient and sustainable agricultural practices.
    """)
