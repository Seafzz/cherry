import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os

def performance_page():
    st.title('Performance')
    st.write("This page displays the performance metrics of the machine learning model.")

    # Example of loading metrics (accuracy, precision, recall, etc.)
    metrics = {
        "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
        "Value": [0.95, 0.94, 0.93, 0.93]  # Placeholder values, replace with actual metrics
    }
    metrics_df = pd.DataFrame(metrics)  # Convert dictionary to DataFrame
    st.write(metrics_df)

    # Example of showing performance plots
    version = 'v1'
    
    training_acc_path = f'outputs/{version}/model_training_acc.png'
    training_losses_path = f'outputs/{version}/model_training_losses.png'
    labels_distribution_path = f'outputs/{version}/labels_distribution.png'

    if os.path.exists(training_acc_path):
        st.image(training_acc_path, caption='Model Training Accuracy')

    if os.path.exists(training_losses_path):
        st.image(training_losses_path, caption='Model Training Losses')

    if os.path.exists(labels_distribution_path):
        st.image(labels_distribution_path, caption='Labels Distribution')

    confusion_matrix_path = f'outputs/{version}/confusion_matrix.png'
    if os.path.exists(confusion_matrix_path):
        confusion_matrix = plt.imread(confusion_matrix_path)
        st.image(confusion_matrix, caption='Confusion Matrix')
    else:
        st.error("The confusion matrix file is missing.")

performance_page()

