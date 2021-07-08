"""src/{{cookiecutter.package_name}}/__main__.py"""
import streamlit as st

def main() -> None:
    """{{cookiecutter.friendly_name}}."""
    st.write("Hello, {{cookiecutter.friendly_name}}!")

if __name__ == "__main__":
    main(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover
