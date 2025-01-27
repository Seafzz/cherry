import streamlit as st

def feedback_page():
    st.title('Feedback')
    st.write("We would love to hear your thoughts and suggestions. Please provide your feedback below:")
    feedback = st.text_area("Your Feedback", "")
    if st.button("Submit"):
        with open("feedback.txt", "a") as file:
            file.write(feedback + "\n")
        st.success("Thank you for your feedback!")

feedback_page()
