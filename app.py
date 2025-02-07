import streamlit as st
from app_pages.multipage import MultiPage

# Load page scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_hypothesis import hypothesis_page
from app_pages.page_data_visualizer import visual_page
from app_pages.page_data_prediction import prediction_page
from app_pages.page_performance import performance_page
from app_pages.page_feedback import feedback_page

# Initialize the app
app = MultiPage(app_name='Cherry Leaves')

# Add pages to the app
app.add_page("Summary", page_summary_body)
app.add_page("Hypothesis", hypothesis_page)
app.add_page("Data Visualizer", visual_page)
app.add_page("Prediction", prediction_page)
app.add_page("Performance", performance_page)
app.add_page("Feedback", feedback_page)

# Run the app
app.run()

