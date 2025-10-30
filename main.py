import streamlit as st
import codecs


# Function to read and render HTML
def render_html_component(file_path, height=600):
    with codecs.open(file_path, 'r') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=height, scrolling=False)


# Assuming you have an 'advanced_calculator.html' file
render_html_component("advanced_calculator.html", height=650)
