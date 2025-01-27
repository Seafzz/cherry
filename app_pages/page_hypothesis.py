import streamlit as st

def hypothesis_page():
    st.title('Hypothesis')

    st.header("Research Hypotheses")
    st.write("""
    The following hypotheses are formulated to guide the Cherry Leaves Classification Project:

    1. **Visual Differentiation Hypothesis**: Healthy cherry leaves and those infected with powdery mildew can be visually differentiated based on their features in images.
    
    2. **Predictive Model Hypothesis**: A convolutional neural network (CNN) can be trained to accurately classify cherry leaves as either healthy or infected with powdery mildew.
    
    3. **Scalability Hypothesis**: The implementation of a machine learning model can significantly reduce the time and manual effort required for inspecting cherry leaves, making the process scalable to multiple farms.
    """)

    st.header("Supporting Rationale")
    st.write("""
    - **Image-Based Analysis**: Previous research indicates that image-based analysis can effectively identify visual signs of plant diseases.
    
    - **CNN Effectiveness**: Convolutional neural networks have shown high accuracy in image classification tasks, including medical imaging and agricultural applications.
    
    - **Efficiency Improvement**: Automating the inspection process with a trained model can vastly improve efficiency and allow for real-time decision-making, reducing the need for extensive manual labor.
    """)

    st.header("Expected Outcomes")
    st.write("""
    - Development of a reliable image classification model for cherry leaves.
    
    - Visual and quantitative evidence supporting the differentiation between healthy and infected leaves.
    
    - A demonstrable reduction in the time required for inspecting cherry trees, with potential for scalability to other crops.
    """)

# Call the function to display the content
hypothesis_page()
