import streamlit as st
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import random

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(os.path.join(dir_path, label_to_display))
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            st.error(f"Reduce the number of rows or columns. There are {len(images_list)} images, but you requested {nrows * ncols} slots.")
            return

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows * ncols):
            img = imread(os.path.join(dir_path, label_to_display, img_idx[x]))
            img_shape = img.shape
            axes[x // ncols, x % ncols].imshow(img)
            axes[x // ncols, x % ncols].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[x // ncols, x % ncols].set_xticks([])
            axes[x // ncols, x % ncols].set_yticks([])
        plt.tight_layout()
        st.pyplot(fig=fig)
    else:
        st.error(f"Label '{label_to_display}' does not exist. Available options are: {labels}")

def visual_page():
    st.title('Data Visualizer')
    st.info("Visualize different aspects of the cherry leaves dataset.")

    version = 'v1'
    if st.checkbox("Average and Variability Images"):
        avg_mildew_path = f"outputs/{version}/avg_var_powdery_mildew.png"
        avg_healthy_path = f"outputs/{version}/avg_var_healthy.png"
        if os.path.exists(avg_mildew_path) and os.path.exists(avg_healthy_path):
            avg_mildew = plt.imread(avg_mildew_path)
            avg_healthy = plt.imread(avg_healthy_path)
            st.warning("Average and Variability images show the overall appearance and color variation within the sets of healthy and infected leaves.")
            st.image(avg_mildew, caption='Powdery Mildew Leaf - Average and Variability')
            st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        else:
            st.error("One or both of the average images are missing.")
        st.write("---")

    if st.checkbox("Difference between Average Images"):
        diff_between_avgs_path = f"outputs/{version}/avg_diff.png"
        if os.path.exists(diff_between_avgs_path):
            diff_between_avgs = plt.imread(diff_between_avgs_path)
            st.warning("This image highlights the differences between average images of healthy and infected leaves, showing clear variations along the edges.")
            st.image(diff_between_avgs, caption='Difference between average images')
        else:
            st.error("The difference between average images file is missing.")
        st.write("---")

    if st.checkbox("Image Montage"):
        st.write("* Click on the 'Create Montage' button to generate a new montage.")
        data_dir = 'inputs/cherry_dataset/cherry-leaves'
        labels = os.listdir(os.path.join(data_dir, 'validation'))
        label_to_display = st.selectbox("Select Label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=os.path.join(data_dir, 'validation'), label_to_display=label_to_display, nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")

visual_page()

