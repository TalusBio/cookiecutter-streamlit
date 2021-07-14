"""apps/streamlit_app.py"""
import streamlit as st

st.set_page_config(
    page_title="{{cookiecutter.friendly_name}}",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main() -> None:
    """{{cookiecutter.friendly_name}}."""
    st.write("Hello, {{cookiecutter.friendly_name}}!")

if __name__ == "__main__":
    main()